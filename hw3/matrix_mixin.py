import numpy as np
import numbers


class Print2DMixin:
    def __str__(self):
        return "[" + "\n".join(["\t".join(["["] + [str(x) for x in row] + ["]"]) for row in self]) + "]"


class SaveMixin:
    def save(self, path):
        with open(path, "w") as f:
            f.write(str(self))


class FieldsMixin:
    def __init__(self, value):
        self._value = np.asarray(value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def shape(self):
        return self._value.shape

    def __len__(self):
        return len(self._value)

    def __getitem__(self, item):
        return self._value[item]


class IterMixin:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        self.c = 0
        return self

    def __next__(self):
        if self.c < len(self.value):
            i = self.c
            self.c += 1
            return self.value[i]
        else:
            raise StopIteration


# по примеру отсюда: https://numpy.org/doc/stable/reference/generated/numpy.lib.mixins.NDArrayOperatorsMixin.html
class MixinMatrix(np.lib.mixins.NDArrayOperatorsMixin, FieldsMixin, IterMixin, Print2DMixin, SaveMixin):
    def __init__(self, value):
        self.value = np.asarray(value)

    _HANDLED_TYPES = (np.ndarray, numbers.Number)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())
        for x in inputs + out:
            if not isinstance(x, self._HANDLED_TYPES + (MixinMatrix,)):
                return NotImplemented
        inputs = tuple(x.value if isinstance(x, MixinMatrix) else x
                       for x in inputs)
        if out:
            kwargs['out'] = tuple(
                x.value if isinstance(x, MixinMatrix) else x
                for x in out)
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            return None
        else:
            return type(self)(result)

    def __repr__(self):
        return '%s(%r)' % (type(self).__name__, self.value)
