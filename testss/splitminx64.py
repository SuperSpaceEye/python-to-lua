def splitminx64_stateless(index):
    z = index + 0x9E3779B97F4A7C15
    z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9
    z = (z ^ (z >> 27)) * 0x94D049BB133111EB
    return z ^ (z>>31)

class splitminx64:
    def __init__(self, seed):
        self.splitminx64_x = seed
    def __call__(self, *args, **kwargs):
        self.splitminx64_x += 0x9E3779B97F4A7C15
        z = self.splitminx64_x
        z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9
        z = (z ^ (z >> 27)) * 0x94D049BB133111EB
        return z ^ (z >> 31)