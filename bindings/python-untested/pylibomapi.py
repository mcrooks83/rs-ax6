r"""Wrapper for omapi.h

Generated with:
ctypesgen/run.py -a -l ../../src/libomapi.a -o rspy-libomapi.py ../../include/omapi.h

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python

import ctypes
import sys
from ctypes import *  # noqa: F401, F403

_int_types = (ctypes.c_int16, ctypes.c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have ctypes.c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (ctypes.c_int64,)
for t in _int_types:
    if ctypes.sizeof(t) == ctypes.sizeof(ctypes.c_size_t):
        c_ptrdiff_t = t
del t
del _int_types



class UserString:
    def __init__(self, seq):
        if isinstance(seq, bytes):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq).encode()

    def __bytes__(self):
        return self.data

    def __str__(self):
        return self.data.decode()

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data.decode())

    def __long__(self):
        return int(self.data.decode())

    def __float__(self):
        return float(self.data.decode())

    def __complex__(self):
        return complex(self.data.decode())

    def __hash__(self):
        return hash(self.data)

    def __le__(self, string):
        if isinstance(string, UserString):
            return self.data <= string.data
        else:
            return self.data <= string

    def __lt__(self, string):
        if isinstance(string, UserString):
            return self.data < string.data
        else:
            return self.data < string

    def __ge__(self, string):
        if isinstance(string, UserString):
            return self.data >= string.data
        else:
            return self.data >= string

    def __gt__(self, string):
        if isinstance(string, UserString):
            return self.data > string.data
        else:
            return self.data > string

    def __eq__(self, string):
        if isinstance(string, UserString):
            return self.data == string.data
        else:
            return self.data == string

    def __ne__(self, string):
        if isinstance(string, UserString):
            return self.data != string.data
        else:
            return self.data != string

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, bytes):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other).encode())

    def __radd__(self, other):
        if isinstance(other, bytes):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other).encode() + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1 :]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1 :]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(sub, bytes):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub).encode() + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, bytes):
            self.data += other
        else:
            self.data += str(other).encode()
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, ctypes.Union):

    _fields_ = [("raw", ctypes.POINTER(ctypes.c_char)), ("data", ctypes.c_char_p)]

    def __init__(self, obj=b""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(ctypes.POINTER(ctypes.c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from bytes
        elif isinstance(obj, bytes):
            return cls(obj)

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj.encode())

        # Convert from c_char_p
        elif isinstance(obj, ctypes.c_char_p):
            return obj

        # Convert from POINTER(ctypes.c_char)
        elif isinstance(obj, ctypes.POINTER(ctypes.c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(ctypes.cast(obj, ctypes.POINTER(ctypes.c_char)))

        # Convert from ctypes.c_char array
        elif isinstance(obj, ctypes.c_char * len(obj)):
            return obj

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)


# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to ctypes.c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P":
        return type
    else:
        return ctypes.c_void_p


# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes, errcheck):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes
        if errcheck:
            self.func.errcheck = errcheck

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))


def ord_if_char(value):
    """
    Simple helper used for casts to simple builtin types:  if the argument is a
    string type, it will be converted to it's ordinal value.

    This function will raise an exception if the argument is string with more
    than one characters.
    """
    return ord(value) if (isinstance(value, bytes) or isinstance(value, str)) else value

# End preamble

_libs = {}
_libdirs = []

# Begin loader

"""
Load libraries - appropriately for all our supported platforms
"""
# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import ctypes
import ctypes.util
import glob
import os.path
import platform
import re
import sys


def _environ_path(name):
    """Split an environment variable into a path-like list elements"""
    if name in os.environ:
        return os.environ[name].split(":")
    return []


class LibraryLoader:
    """
    A base class For loading of libraries ;-)
    Subclasses load libraries for specific platforms.
    """

    # library names formatted specifically for platforms
    name_formats = ["%s"]

    class Lookup:
        """Looking up calling conventions for a platform"""

        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode))

        def get(self, name, calling_convention="cdecl"):
            """Return the given name according to the selected calling convention"""
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".format(
                        calling_convention, name
                    )
                )
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention="cdecl"):
            """Return True if this given calling convention finds the given 'name'"""
            if calling_convention not in self.access:
                return False
            return hasattr(self.access[calling_convention], name)

        def __getattr__(self, name):
            return getattr(self.access["cdecl"], name)

    def __init__(self):
        self.other_dirs = []

    def __call__(self, libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            # noinspection PyBroadException
            try:
                return self.Lookup(path)
            except Exception:  # pylint: disable=broad-except
                pass

        raise ImportError("Could not load %s." % libname)

    def getpaths(self, libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # search through a prioritized series of locations for the library

            # we first search any specific directories identified by user
            for dir_i in self.other_dirs:
                for fmt in self.name_formats:
                    # dir_i should be absolute already
                    yield os.path.join(dir_i, fmt % libname)

            # check if this code is even stored in a physical file
            try:
                this_file = __file__
            except NameError:
                this_file = None

            # then we search the directory where the generated python interface is stored
            if this_file is not None:
                for fmt in self.name_formats:
                    yield os.path.abspath(os.path.join(os.path.dirname(__file__), fmt % libname))

            # now, use the ctypes tools to try to find the library
            for fmt in self.name_formats:
                path = ctypes.util.find_library(fmt % libname)
                if path:
                    yield path

            # then we search all paths identified as platform-specific lib paths
            for path in self.getplatformpaths(libname):
                yield path

            # Finally, we'll try the users current working directory
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.curdir, fmt % libname))

    def getplatformpaths(self, _libname):  # pylint: disable=no-self-use
        """Return all the library paths available in this platform"""
        return []


# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    """Library loader for MacOS"""

    name_formats = [
        "lib%s.dylib",
        "lib%s.so",
        "lib%s.bundle",
        "%s.dylib",
        "%s.so",
        "%s.bundle",
        "%s",
    ]

    class Lookup(LibraryLoader.Lookup):
        """
        Looking up library files for this platform (Darwin aka MacOS)
        """

        # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
        # of the default RTLD_LOCAL.  Without this, you end up with
        # libraries not being loadable, resulting in "Symbol not found"
        # errors
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [fmt % libname for fmt in self.name_formats]

        for directory in self.getdirs(libname):
            for name in names:
                yield os.path.join(directory, name)

    @staticmethod
    def getdirs(libname):
        """Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [
                os.path.expanduser("~/lib"),
                "/usr/local/lib",
                "/usr/lib",
            ]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
            dirs.extend(_environ_path("LD_RUN_PATH"))

        if hasattr(sys, "frozen") and getattr(sys, "frozen") == "macosx_app":
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    """Library loader for POSIX-like systems (including Linux)"""

    _ld_so_cache = None

    _include = re.compile(r"^\s*include\s+(?P<pattern>.*)")

    name_formats = ["lib%s.so", "%s.so", "%s"]

    class _Directories(dict):
        """Deal with directories"""

        def __init__(self):
            dict.__init__(self)
            self.order = 0

        def add(self, directory):
            """Add a directory to our current set of directories"""
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
            # only adds and updates order if exists and not already in set
            if not os.path.exists(directory):
                return
            order = self.setdefault(directory, self.order)
            if order == self.order:
                self.order += 1

        def extend(self, directories):
            """Add a list of directories to our set"""
            for a_dir in directories:
                self.add(a_dir)

        def ordered(self):
            """Sort the list of directories"""
            return (i[0] for i in sorted(self.items(), key=lambda d: d[1]))

    def _get_ld_so_conf_dirs(self, conf, dirs):
        """
        Recursive function to help parse all ld.so.conf files, including proper
        handling of the `include` directive.
        """

        try:
            with open(conf) as fileobj:
                for dirname in fileobj:
                    dirname = dirname.strip()
                    if not dirname:
                        continue

                    match = self._include.match(dirname)
                    if not match:
                        dirs.add(dirname)
                    else:
                        for dir2 in glob.glob(match.group("pattern")):
                            self._get_ld_so_conf_dirs(dir2, dirs)
        except IOError:
            pass

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = self._Directories()
        for name in (
            "LD_LIBRARY_PATH",
            "SHLIB_PATH",  # HP-UX
            "LIBPATH",  # OS/2, AIX
            "LIBRARY_PATH",  # BE/OS
        ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))

        self._get_ld_so_conf_dirs("/etc/ld.so.conf", directories)

        bitage = platform.architecture()[0]

        unix_lib_dirs_list = []
        if bitage.startswith("64"):
            # prefer 64 bit if that is our arch
            unix_lib_dirs_list += ["/lib64", "/usr/lib64"]

        # must include standard libs, since those paths are also used by 64 bit
        # installs
        unix_lib_dirs_list += ["/lib", "/usr/lib"]
        if sys.platform.startswith("linux"):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            if bitage.startswith("32"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/i386-linux-gnu", "/usr/lib/i386-linux-gnu"]
            elif bitage.startswith("64"):
                # Assume Intel/AMD x86 compatible
                unix_lib_dirs_list += [
                    "/lib/x86_64-linux-gnu",
                    "/usr/lib/x86_64-linux-gnu",
                ]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        # ext_re = re.compile(r"\.s[ol]$")
        for our_dir in directories.ordered():
            try:
                for path in glob.glob("%s/*.s[ol]*" % our_dir):
                    file = os.path.basename(path)

                    # Index by filename
                    cache_i = cache.setdefault(file, set())
                    cache_i.add(path)

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        cache_i = cache.setdefault(library, set())
                        cache_i.add(path)
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname, set())
        for i in result:
            # we iterate through all found paths for library, since we may have
            # actually found multiple architectures or other library types that
            # may not load
            yield i


# Windows


class WindowsLibraryLoader(LibraryLoader):
    """Library loader for Microsoft Windows"""

    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll", "%s"]

    class Lookup(LibraryLoader.Lookup):
        """Lookup class for Windows libraries..."""

        def __init__(self, path):
            super(WindowsLibraryLoader.Lookup, self).__init__(path)
            self.access["stdcall"] = ctypes.windll.LoadLibrary(path)


# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin": DarwinLibraryLoader,
    "cygwin": WindowsLibraryLoader,
    "win32": WindowsLibraryLoader,
    "msys": WindowsLibraryLoader,
}

load_library = loaderclass.get(sys.platform, PosixLibraryLoader)()


def add_library_search_dirs(other_dirs):
    """
    Add libraries to search paths.
    If library paths are relative, convert them to absolute with respect to this
    file's directory
    """
    for path in other_dirs:
        if not os.path.isabs(path):
            path = os.path.abspath(path)
        load_library.other_dirs.append(path)


del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries
_libs["../../src/libomapi.a"] = load_library("../../src/libomapi.a")

# 1 libraries
# End libraries

# No modules

size_t = c_ulong# /usr/lib/gcc/x86_64-linux-gnu/9/include/stddef.h: 209

wchar_t = c_int# /usr/lib/gcc/x86_64-linux-gnu/9/include/stddef.h: 321

enum_anon_1 = c_int# /usr/include/x86_64-linux-gnu/bits/waitflags.h: 57

idtype_t = enum_anon_1# /usr/include/x86_64-linux-gnu/bits/waitflags.h: 57

_Float32 = c_float# /usr/include/x86_64-linux-gnu/bits/floatn-common.h: 214

_Float64 = c_double# /usr/include/x86_64-linux-gnu/bits/floatn-common.h: 251

_Float32x = c_double# /usr/include/x86_64-linux-gnu/bits/floatn-common.h: 268

_Float64x = c_longdouble# /usr/include/x86_64-linux-gnu/bits/floatn-common.h: 285

# /usr/include/stdlib.h: 62
class struct_anon_2(Structure):
    pass

struct_anon_2.__slots__ = [
    'quot',
    'rem',
]
struct_anon_2._fields_ = [
    ('quot', c_int),
    ('rem', c_int),
]

div_t = struct_anon_2# /usr/include/stdlib.h: 62

# /usr/include/stdlib.h: 70
class struct_anon_3(Structure):
    pass

struct_anon_3.__slots__ = [
    'quot',
    'rem',
]
struct_anon_3._fields_ = [
    ('quot', c_long),
    ('rem', c_long),
]

ldiv_t = struct_anon_3# /usr/include/stdlib.h: 70

# /usr/include/stdlib.h: 80
class struct_anon_4(Structure):
    pass

struct_anon_4.__slots__ = [
    'quot',
    'rem',
]
struct_anon_4._fields_ = [
    ('quot', c_longlong),
    ('rem', c_longlong),
]

lldiv_t = struct_anon_4# /usr/include/stdlib.h: 80

# /usr/include/stdlib.h: 97
for _lib in _libs.values():
    if not _lib.has("__ctype_get_mb_cur_max", "cdecl"):
        continue
    __ctype_get_mb_cur_max = _lib.get("__ctype_get_mb_cur_max", "cdecl")
    __ctype_get_mb_cur_max.argtypes = []
    __ctype_get_mb_cur_max.restype = c_size_t
    break

# /usr/include/stdlib.h: 101
for _lib in _libs.values():
    if not _lib.has("atof", "cdecl"):
        continue
    atof = _lib.get("atof", "cdecl")
    atof.argtypes = [String]
    atof.restype = c_double
    break

# /usr/include/stdlib.h: 104
for _lib in _libs.values():
    if not _lib.has("atoi", "cdecl"):
        continue
    atoi = _lib.get("atoi", "cdecl")
    atoi.argtypes = [String]
    atoi.restype = c_int
    break

# /usr/include/stdlib.h: 107
for _lib in _libs.values():
    if not _lib.has("atol", "cdecl"):
        continue
    atol = _lib.get("atol", "cdecl")
    atol.argtypes = [String]
    atol.restype = c_long
    break

# /usr/include/stdlib.h: 112
for _lib in _libs.values():
    if not _lib.has("atoll", "cdecl"):
        continue
    atoll = _lib.get("atoll", "cdecl")
    atoll.argtypes = [String]
    atoll.restype = c_longlong
    break

# /usr/include/stdlib.h: 385
for _lib in _libs.values():
    if not _lib.has("l64a", "cdecl"):
        continue
    l64a = _lib.get("l64a", "cdecl")
    l64a.argtypes = [c_long]
    if sizeof(c_int) == sizeof(c_void_p):
        l64a.restype = ReturnString
    else:
        l64a.restype = String
        l64a.errcheck = ReturnString
    break

# /usr/include/stdlib.h: 388
for _lib in _libs.values():
    if not _lib.has("a64l", "cdecl"):
        continue
    a64l = _lib.get("a64l", "cdecl")
    a64l.argtypes = [String]
    a64l.restype = c_long
    break

__u_char = c_ubyte# /usr/include/x86_64-linux-gnu/bits/types.h: 31

__u_short = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 32

__u_int = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 33

__u_long = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 34

__int8_t = c_char# /usr/include/x86_64-linux-gnu/bits/types.h: 37

__uint8_t = c_ubyte# /usr/include/x86_64-linux-gnu/bits/types.h: 38

__int16_t = c_int# /usr/include/x86_64-linux-gnu/bits/types.h: 39

__uint16_t = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 40

__int32_t = c_int# /usr/include/x86_64-linux-gnu/bits/types.h: 41

__uint32_t = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 42

__int64_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 44

__uint64_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 45

__int_least8_t = __int8_t# /usr/include/x86_64-linux-gnu/bits/types.h: 52

__uint_least8_t = __uint8_t# /usr/include/x86_64-linux-gnu/bits/types.h: 53

__int_least16_t = __int16_t# /usr/include/x86_64-linux-gnu/bits/types.h: 54

__uint_least16_t = __uint16_t# /usr/include/x86_64-linux-gnu/bits/types.h: 55

__int_least32_t = __int32_t# /usr/include/x86_64-linux-gnu/bits/types.h: 56

__uint_least32_t = __uint32_t# /usr/include/x86_64-linux-gnu/bits/types.h: 57

__int_least64_t = __int64_t# /usr/include/x86_64-linux-gnu/bits/types.h: 58

__uint_least64_t = __uint64_t# /usr/include/x86_64-linux-gnu/bits/types.h: 59

__quad_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 63

__u_quad_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 64

__intmax_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 72

__uintmax_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 73

__dev_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 145

__uid_t = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 146

__gid_t = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 147

__ino_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 148

__ino64_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 149

__mode_t = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 150

__nlink_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 151

__off_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 152

__off64_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 153

__pid_t = c_int# /usr/include/x86_64-linux-gnu/bits/types.h: 154

# /usr/include/x86_64-linux-gnu/bits/types.h: 155
class struct_anon_5(Structure):
    pass

struct_anon_5.__slots__ = [
    '__val',
]
struct_anon_5._fields_ = [
    ('__val', c_int * int(2)),
]

__fsid_t = struct_anon_5# /usr/include/x86_64-linux-gnu/bits/types.h: 155

__clock_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 156

__rlim_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 157

__rlim64_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 158

__id_t = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 159

__time_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 160

__useconds_t = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 161

__suseconds_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 162

__daddr_t = c_int# /usr/include/x86_64-linux-gnu/bits/types.h: 164

__key_t = c_int# /usr/include/x86_64-linux-gnu/bits/types.h: 165

__clockid_t = c_int# /usr/include/x86_64-linux-gnu/bits/types.h: 168

__timer_t = POINTER(None)# /usr/include/x86_64-linux-gnu/bits/types.h: 171

__blksize_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 174

__blkcnt_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 179

__blkcnt64_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 180

__fsblkcnt_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 183

__fsblkcnt64_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 184

__fsfilcnt_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 187

__fsfilcnt64_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 188

__fsword_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 191

__ssize_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 193

__syscall_slong_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 196

__syscall_ulong_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 198

__loff_t = __off64_t# /usr/include/x86_64-linux-gnu/bits/types.h: 202

__caddr_t = String# /usr/include/x86_64-linux-gnu/bits/types.h: 203

__intptr_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 206

__socklen_t = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 209

__sig_atomic_t = c_int# /usr/include/x86_64-linux-gnu/bits/types.h: 214

u_char = __u_char# /usr/include/x86_64-linux-gnu/sys/types.h: 33

u_short = __u_short# /usr/include/x86_64-linux-gnu/sys/types.h: 34

u_int = __u_int# /usr/include/x86_64-linux-gnu/sys/types.h: 35

u_long = __u_long# /usr/include/x86_64-linux-gnu/sys/types.h: 36

quad_t = __quad_t# /usr/include/x86_64-linux-gnu/sys/types.h: 37

u_quad_t = __u_quad_t# /usr/include/x86_64-linux-gnu/sys/types.h: 38

fsid_t = __fsid_t# /usr/include/x86_64-linux-gnu/sys/types.h: 39

loff_t = __loff_t# /usr/include/x86_64-linux-gnu/sys/types.h: 42

ino_t = __ino_t# /usr/include/x86_64-linux-gnu/sys/types.h: 47

dev_t = __dev_t# /usr/include/x86_64-linux-gnu/sys/types.h: 59

gid_t = __gid_t# /usr/include/x86_64-linux-gnu/sys/types.h: 64

mode_t = __mode_t# /usr/include/x86_64-linux-gnu/sys/types.h: 69

nlink_t = __nlink_t# /usr/include/x86_64-linux-gnu/sys/types.h: 74

uid_t = __uid_t# /usr/include/x86_64-linux-gnu/sys/types.h: 79

off_t = __off_t# /usr/include/x86_64-linux-gnu/sys/types.h: 85

pid_t = __pid_t# /usr/include/x86_64-linux-gnu/sys/types.h: 97

id_t = __id_t# /usr/include/x86_64-linux-gnu/sys/types.h: 103

ssize_t = __ssize_t# /usr/include/x86_64-linux-gnu/sys/types.h: 108

daddr_t = __daddr_t# /usr/include/x86_64-linux-gnu/sys/types.h: 114

caddr_t = __caddr_t# /usr/include/x86_64-linux-gnu/sys/types.h: 115

key_t = __key_t# /usr/include/x86_64-linux-gnu/sys/types.h: 121

clock_t = __clock_t# /usr/include/x86_64-linux-gnu/bits/types/clock_t.h: 7

clockid_t = __clockid_t# /usr/include/x86_64-linux-gnu/bits/types/clockid_t.h: 7

time_t = __time_t# /usr/include/x86_64-linux-gnu/bits/types/time_t.h: 7

timer_t = __timer_t# /usr/include/x86_64-linux-gnu/bits/types/timer_t.h: 7

ulong = c_ulong# /usr/include/x86_64-linux-gnu/sys/types.h: 148

ushort = c_uint# /usr/include/x86_64-linux-gnu/sys/types.h: 149

uint = c_uint# /usr/include/x86_64-linux-gnu/sys/types.h: 150

int8_t = __int8_t# /usr/include/x86_64-linux-gnu/bits/stdint-intn.h: 24

int16_t = __int16_t# /usr/include/x86_64-linux-gnu/bits/stdint-intn.h: 25

int32_t = __int32_t# /usr/include/x86_64-linux-gnu/bits/stdint-intn.h: 26

int64_t = __int64_t# /usr/include/x86_64-linux-gnu/bits/stdint-intn.h: 27

u_int8_t = __uint8_t# /usr/include/x86_64-linux-gnu/sys/types.h: 158

u_int16_t = __uint16_t# /usr/include/x86_64-linux-gnu/sys/types.h: 159

u_int32_t = __uint32_t# /usr/include/x86_64-linux-gnu/sys/types.h: 160

u_int64_t = __uint64_t# /usr/include/x86_64-linux-gnu/sys/types.h: 161

register_t = c_int# /usr/include/x86_64-linux-gnu/sys/types.h: 166

# /usr/include/x86_64-linux-gnu/bits/types/__sigset_t.h: 8
class struct_anon_6(Structure):
    pass

struct_anon_6.__slots__ = [
    '__val',
]
struct_anon_6._fields_ = [
    ('__val', c_ulong * int((1024 / (8 * sizeof(c_ulong))))),
]

__sigset_t = struct_anon_6# /usr/include/x86_64-linux-gnu/bits/types/__sigset_t.h: 8

sigset_t = __sigset_t# /usr/include/x86_64-linux-gnu/bits/types/sigset_t.h: 7

# /usr/include/x86_64-linux-gnu/bits/types/struct_timeval.h: 8
class struct_timeval(Structure):
    pass

struct_timeval.__slots__ = [
    'tv_sec',
    'tv_usec',
]
struct_timeval._fields_ = [
    ('tv_sec', __time_t),
    ('tv_usec', __suseconds_t),
]

# /usr/include/x86_64-linux-gnu/bits/types/struct_timespec.h: 10
class struct_timespec(Structure):
    pass

struct_timespec.__slots__ = [
    'tv_sec',
    'tv_nsec',
]
struct_timespec._fields_ = [
    ('tv_sec', __time_t),
    ('tv_nsec', __syscall_slong_t),
]

suseconds_t = __suseconds_t# /usr/include/x86_64-linux-gnu/sys/select.h: 43

__fd_mask = c_long# /usr/include/x86_64-linux-gnu/sys/select.h: 49

# /usr/include/x86_64-linux-gnu/sys/select.h: 70
class struct_anon_7(Structure):
    pass

struct_anon_7.__slots__ = [
    '__fds_bits',
]
struct_anon_7._fields_ = [
    ('__fds_bits', __fd_mask * int((1024 / (8 * (c_int (ord_if_char(sizeof(__fd_mask)))).value)))),
]

fd_set = struct_anon_7# /usr/include/x86_64-linux-gnu/sys/select.h: 70

fd_mask = __fd_mask# /usr/include/x86_64-linux-gnu/sys/select.h: 77

blksize_t = __blksize_t# /usr/include/x86_64-linux-gnu/sys/types.h: 185

blkcnt_t = __blkcnt_t# /usr/include/x86_64-linux-gnu/sys/types.h: 192

fsblkcnt_t = __fsblkcnt_t# /usr/include/x86_64-linux-gnu/sys/types.h: 196

fsfilcnt_t = __fsfilcnt_t# /usr/include/x86_64-linux-gnu/sys/types.h: 200

# /usr/include/x86_64-linux-gnu/bits/thread-shared-types.h: 49
class struct___pthread_internal_list(Structure):
    pass

struct___pthread_internal_list.__slots__ = [
    '__prev',
    '__next',
]
struct___pthread_internal_list._fields_ = [
    ('__prev', POINTER(struct___pthread_internal_list)),
    ('__next', POINTER(struct___pthread_internal_list)),
]

__pthread_list_t = struct___pthread_internal_list# /usr/include/x86_64-linux-gnu/bits/thread-shared-types.h: 53

# /usr/include/x86_64-linux-gnu/bits/thread-shared-types.h: 55
class struct___pthread_internal_slist(Structure):
    pass

struct___pthread_internal_slist.__slots__ = [
    '__next',
]
struct___pthread_internal_slist._fields_ = [
    ('__next', POINTER(struct___pthread_internal_slist)),
]

__pthread_slist_t = struct___pthread_internal_slist# /usr/include/x86_64-linux-gnu/bits/thread-shared-types.h: 58

# /usr/include/x86_64-linux-gnu/bits/struct_mutex.h: 22
class struct___pthread_mutex_s(Structure):
    pass

struct___pthread_mutex_s.__slots__ = [
    '__lock',
    '__count',
    '__owner',
    '__nusers',
    '__kind',
    '__spins',
    '__elision',
    '__list',
]
struct___pthread_mutex_s._fields_ = [
    ('__lock', c_int),
    ('__count', c_uint),
    ('__owner', c_int),
    ('__nusers', c_uint),
    ('__kind', c_int),
    ('__spins', c_short),
    ('__elision', c_short),
    ('__list', __pthread_list_t),
]

# /usr/include/x86_64-linux-gnu/bits/struct_rwlock.h: 23
class struct___pthread_rwlock_arch_t(Structure):
    pass

struct___pthread_rwlock_arch_t.__slots__ = [
    '__readers',
    '__writers',
    '__wrphase_futex',
    '__writers_futex',
    '__pad3',
    '__pad4',
    '__cur_writer',
    '__shared',
    '__rwelision',
    '__pad1',
    '__pad2',
    '__flags',
]
struct___pthread_rwlock_arch_t._fields_ = [
    ('__readers', c_uint),
    ('__writers', c_uint),
    ('__wrphase_futex', c_uint),
    ('__writers_futex', c_uint),
    ('__pad3', c_uint),
    ('__pad4', c_uint),
    ('__cur_writer', c_int),
    ('__shared', c_int),
    ('__rwelision', c_char),
    ('__pad1', c_ubyte * int(7)),
    ('__pad2', c_ulong),
    ('__flags', c_uint),
]

# /usr/include/x86_64-linux-gnu/bits/thread-shared-types.h: 97
class struct_anon_8(Structure):
    pass

struct_anon_8.__slots__ = [
    '__low',
    '__high',
]
struct_anon_8._fields_ = [
    ('__low', c_uint),
    ('__high', c_uint),
]

# /usr/include/x86_64-linux-gnu/bits/thread-shared-types.h: 94
class union_anon_9(Union):
    pass

union_anon_9.__slots__ = [
    '__wseq',
    '__wseq32',
]
union_anon_9._fields_ = [
    ('__wseq', c_ulonglong),
    ('__wseq32', struct_anon_8),
]

# /usr/include/x86_64-linux-gnu/bits/thread-shared-types.h: 106
class struct_anon_10(Structure):
    pass

struct_anon_10.__slots__ = [
    '__low',
    '__high',
]
struct_anon_10._fields_ = [
    ('__low', c_uint),
    ('__high', c_uint),
]

# /usr/include/x86_64-linux-gnu/bits/thread-shared-types.h: 103
class union_anon_11(Union):
    pass

union_anon_11.__slots__ = [
    '__g1_start',
    '__g1_start32',
]
union_anon_11._fields_ = [
    ('__g1_start', c_ulonglong),
    ('__g1_start32', struct_anon_10),
]

# /usr/include/x86_64-linux-gnu/bits/thread-shared-types.h: 92
class struct___pthread_cond_s(Structure):
    pass

struct___pthread_cond_s.__slots__ = [
    'unnamed_1',
    'unnamed_2',
    '__g_refs',
    '__g_size',
    '__g1_orig_size',
    '__wrefs',
    '__g_signals',
]
struct___pthread_cond_s._anonymous_ = [
    'unnamed_1',
    'unnamed_2',
]
struct___pthread_cond_s._fields_ = [
    ('unnamed_1', union_anon_9),
    ('unnamed_2', union_anon_11),
    ('__g_refs', c_uint * int(2)),
    ('__g_size', c_uint * int(2)),
    ('__g1_orig_size', c_uint),
    ('__wrefs', c_uint),
    ('__g_signals', c_uint * int(2)),
]

pthread_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 27

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 36
class union_anon_12(Union):
    pass

union_anon_12.__slots__ = [
    '__size',
    '__align',
]
union_anon_12._fields_ = [
    ('__size', c_char * int(4)),
    ('__align', c_int),
]

pthread_mutexattr_t = union_anon_12# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 36

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 45
class union_anon_13(Union):
    pass

union_anon_13.__slots__ = [
    '__size',
    '__align',
]
union_anon_13._fields_ = [
    ('__size', c_char * int(4)),
    ('__align', c_int),
]

pthread_condattr_t = union_anon_13# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 45

pthread_key_t = c_uint# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 49

pthread_once_t = c_int# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 53

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 56
class union_pthread_attr_t(Union):
    pass

union_pthread_attr_t.__slots__ = [
    '__size',
    '__align',
]
union_pthread_attr_t._fields_ = [
    ('__size', c_char * int(56)),
    ('__align', c_long),
]

pthread_attr_t = union_pthread_attr_t# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 62

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 72
class union_anon_14(Union):
    pass

union_anon_14.__slots__ = [
    '__data',
    '__size',
    '__align',
]
union_anon_14._fields_ = [
    ('__data', struct___pthread_mutex_s),
    ('__size', c_char * int(40)),
    ('__align', c_long),
]

pthread_mutex_t = union_anon_14# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 72

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 80
class union_anon_15(Union):
    pass

union_anon_15.__slots__ = [
    '__data',
    '__size',
    '__align',
]
union_anon_15._fields_ = [
    ('__data', struct___pthread_cond_s),
    ('__size', c_char * int(48)),
    ('__align', c_longlong),
]

pthread_cond_t = union_anon_15# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 80

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 91
class union_anon_16(Union):
    pass

union_anon_16.__slots__ = [
    '__data',
    '__size',
    '__align',
]
union_anon_16._fields_ = [
    ('__data', struct___pthread_rwlock_arch_t),
    ('__size', c_char * int(56)),
    ('__align', c_long),
]

pthread_rwlock_t = union_anon_16# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 91

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 97
class union_anon_17(Union):
    pass

union_anon_17.__slots__ = [
    '__size',
    '__align',
]
union_anon_17._fields_ = [
    ('__size', c_char * int(8)),
    ('__align', c_long),
]

pthread_rwlockattr_t = union_anon_17# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 97

pthread_spinlock_t = c_int# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 103

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 112
class union_anon_18(Union):
    pass

union_anon_18.__slots__ = [
    '__size',
    '__align',
]
union_anon_18._fields_ = [
    ('__size', c_char * int(32)),
    ('__align', c_long),
]

pthread_barrier_t = union_anon_18# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 112

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 118
class union_anon_19(Union):
    pass

union_anon_19.__slots__ = [
    '__size',
    '__align',
]
union_anon_19._fields_ = [
    ('__size', c_char * int(4)),
    ('__align', c_int),
]

pthread_barrierattr_t = union_anon_19# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 118

# /usr/include/stdlib.h: 401
for _lib in _libs.values():
    if not _lib.has("random", "cdecl"):
        continue
    random = _lib.get("random", "cdecl")
    random.argtypes = []
    random.restype = c_long
    break

# /usr/include/stdlib.h: 404
for _lib in _libs.values():
    if not _lib.has("srandom", "cdecl"):
        continue
    srandom = _lib.get("srandom", "cdecl")
    srandom.argtypes = [c_uint]
    srandom.restype = None
    break

# /usr/include/stdlib.h: 410
for _lib in _libs.values():
    if not _lib.has("initstate", "cdecl"):
        continue
    initstate = _lib.get("initstate", "cdecl")
    initstate.argtypes = [c_uint, String, c_size_t]
    if sizeof(c_int) == sizeof(c_void_p):
        initstate.restype = ReturnString
    else:
        initstate.restype = String
        initstate.errcheck = ReturnString
    break

# /usr/include/stdlib.h: 415
for _lib in _libs.values():
    if not _lib.has("setstate", "cdecl"):
        continue
    setstate = _lib.get("setstate", "cdecl")
    setstate.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        setstate.restype = ReturnString
    else:
        setstate.restype = String
        setstate.errcheck = ReturnString
    break

# /usr/include/stdlib.h: 423
class struct_random_data(Structure):
    pass

struct_random_data.__slots__ = [
    'fptr',
    'rptr',
    'state',
    'rand_type',
    'rand_deg',
    'rand_sep',
    'end_ptr',
]
struct_random_data._fields_ = [
    ('fptr', POINTER(c_int32)),
    ('rptr', POINTER(c_int32)),
    ('state', POINTER(c_int32)),
    ('rand_type', c_int),
    ('rand_deg', c_int),
    ('rand_sep', c_int),
    ('end_ptr', POINTER(c_int32)),
]

# /usr/include/stdlib.h: 437
for _lib in _libs.values():
    if not _lib.has("srandom_r", "cdecl"):
        continue
    srandom_r = _lib.get("srandom_r", "cdecl")
    srandom_r.argtypes = [c_uint, POINTER(struct_random_data)]
    srandom_r.restype = c_int
    break

# /usr/include/stdlib.h: 453
for _lib in _libs.values():
    if not _lib.has("rand", "cdecl"):
        continue
    rand = _lib.get("rand", "cdecl")
    rand.argtypes = []
    rand.restype = c_int
    break

# /usr/include/stdlib.h: 455
for _lib in _libs.values():
    if not _lib.has("srand", "cdecl"):
        continue
    srand = _lib.get("srand", "cdecl")
    srand.argtypes = [c_uint]
    srand.restype = None
    break

# /usr/include/stdlib.h: 459
for _lib in _libs.values():
    if not _lib.has("rand_r", "cdecl"):
        continue
    rand_r = _lib.get("rand_r", "cdecl")
    rand_r.argtypes = [POINTER(c_uint)]
    rand_r.restype = c_int
    break

# /usr/include/stdlib.h: 467
for _lib in _libs.values():
    if not _lib.has("drand48", "cdecl"):
        continue
    drand48 = _lib.get("drand48", "cdecl")
    drand48.argtypes = []
    drand48.restype = c_double
    break

# /usr/include/stdlib.h: 468
for _lib in _libs.values():
    if not _lib.has("erand48", "cdecl"):
        continue
    erand48 = _lib.get("erand48", "cdecl")
    erand48.argtypes = [c_uint * int(3)]
    erand48.restype = c_double
    break

# /usr/include/stdlib.h: 471
for _lib in _libs.values():
    if not _lib.has("lrand48", "cdecl"):
        continue
    lrand48 = _lib.get("lrand48", "cdecl")
    lrand48.argtypes = []
    lrand48.restype = c_long
    break

# /usr/include/stdlib.h: 472
for _lib in _libs.values():
    if not _lib.has("nrand48", "cdecl"):
        continue
    nrand48 = _lib.get("nrand48", "cdecl")
    nrand48.argtypes = [c_uint * int(3)]
    nrand48.restype = c_long
    break

# /usr/include/stdlib.h: 476
for _lib in _libs.values():
    if not _lib.has("mrand48", "cdecl"):
        continue
    mrand48 = _lib.get("mrand48", "cdecl")
    mrand48.argtypes = []
    mrand48.restype = c_long
    break

# /usr/include/stdlib.h: 477
for _lib in _libs.values():
    if not _lib.has("jrand48", "cdecl"):
        continue
    jrand48 = _lib.get("jrand48", "cdecl")
    jrand48.argtypes = [c_uint * int(3)]
    jrand48.restype = c_long
    break

# /usr/include/stdlib.h: 481
for _lib in _libs.values():
    if not _lib.has("srand48", "cdecl"):
        continue
    srand48 = _lib.get("srand48", "cdecl")
    srand48.argtypes = [c_long]
    srand48.restype = None
    break

# /usr/include/stdlib.h: 482
for _lib in _libs.values():
    if not _lib.has("seed48", "cdecl"):
        continue
    seed48 = _lib.get("seed48", "cdecl")
    seed48.argtypes = [c_uint * int(3)]
    seed48.restype = POINTER(c_uint)
    break

# /usr/include/stdlib.h: 484
for _lib in _libs.values():
    if not _lib.has("lcong48", "cdecl"):
        continue
    lcong48 = _lib.get("lcong48", "cdecl")
    lcong48.argtypes = [c_uint * int(7)]
    lcong48.restype = None
    break

# /usr/include/stdlib.h: 490
class struct_drand48_data(Structure):
    pass

struct_drand48_data.__slots__ = [
    '__x',
    '__old_x',
    '__c',
    '__init',
    '__a',
]
struct_drand48_data._fields_ = [
    ('__x', c_uint * int(3)),
    ('__old_x', c_uint * int(3)),
    ('__c', c_uint),
    ('__init', c_uint),
    ('__a', c_ulonglong),
]

# /usr/include/stdlib.h: 526
for _lib in _libs.values():
    if not _lib.has("srand48_r", "cdecl"):
        continue
    srand48_r = _lib.get("srand48_r", "cdecl")
    srand48_r.argtypes = [c_long, POINTER(struct_drand48_data)]
    srand48_r.restype = c_int
    break

# /usr/include/stdlib.h: 529
for _lib in _libs.values():
    if not _lib.has("seed48_r", "cdecl"):
        continue
    seed48_r = _lib.get("seed48_r", "cdecl")
    seed48_r.argtypes = [c_uint * int(3), POINTER(struct_drand48_data)]
    seed48_r.restype = c_int
    break

# /usr/include/stdlib.h: 532
for _lib in _libs.values():
    if not _lib.has("lcong48_r", "cdecl"):
        continue
    lcong48_r = _lib.get("lcong48_r", "cdecl")
    lcong48_r.argtypes = [c_uint * int(7), POINTER(struct_drand48_data)]
    lcong48_r.restype = c_int
    break

# /usr/include/stdlib.h: 539
for _lib in _libs.values():
    if not _lib.has("malloc", "cdecl"):
        continue
    malloc = _lib.get("malloc", "cdecl")
    malloc.argtypes = [c_size_t]
    malloc.restype = POINTER(c_ubyte)
    malloc.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /usr/include/stdlib.h: 542
for _lib in _libs.values():
    if not _lib.has("calloc", "cdecl"):
        continue
    calloc = _lib.get("calloc", "cdecl")
    calloc.argtypes = [c_size_t, c_size_t]
    calloc.restype = POINTER(c_ubyte)
    calloc.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /usr/include/stdlib.h: 550
for _lib in _libs.values():
    if not _lib.has("realloc", "cdecl"):
        continue
    realloc = _lib.get("realloc", "cdecl")
    realloc.argtypes = [POINTER(None), c_size_t]
    realloc.restype = POINTER(c_ubyte)
    realloc.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /usr/include/stdlib.h: 559
for _lib in _libs.values():
    if not _lib.has("reallocarray", "cdecl"):
        continue
    reallocarray = _lib.get("reallocarray", "cdecl")
    reallocarray.argtypes = [POINTER(None), c_size_t, c_size_t]
    reallocarray.restype = POINTER(c_ubyte)
    reallocarray.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /usr/include/stdlib.h: 565
for _lib in _libs.values():
    if not _lib.has("free", "cdecl"):
        continue
    free = _lib.get("free", "cdecl")
    free.argtypes = [POINTER(None)]
    free.restype = None
    break

# /usr/include/stdlib.h: 574
for _lib in _libs.values():
    if not _lib.has("valloc", "cdecl"):
        continue
    valloc = _lib.get("valloc", "cdecl")
    valloc.argtypes = [c_size_t]
    valloc.restype = POINTER(c_ubyte)
    valloc.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /usr/include/stdlib.h: 580
for _lib in _libs.values():
    if not _lib.has("posix_memalign", "cdecl"):
        continue
    posix_memalign = _lib.get("posix_memalign", "cdecl")
    posix_memalign.argtypes = [POINTER(POINTER(None)), c_size_t, c_size_t]
    posix_memalign.restype = c_int
    break

# /usr/include/stdlib.h: 586
for _lib in _libs.values():
    if not _lib.has("aligned_alloc", "cdecl"):
        continue
    aligned_alloc = _lib.get("aligned_alloc", "cdecl")
    aligned_alloc.argtypes = [c_size_t, c_size_t]
    aligned_alloc.restype = POINTER(c_ubyte)
    aligned_alloc.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /usr/include/stdlib.h: 591
for _lib in _libs.values():
    if not _lib.has("abort", "cdecl"):
        continue
    abort = _lib.get("abort", "cdecl")
    abort.argtypes = []
    abort.restype = None
    break

# /usr/include/stdlib.h: 595
for _lib in _libs.values():
    if not _lib.has("atexit", "cdecl"):
        continue
    atexit = _lib.get("atexit", "cdecl")
    atexit.argtypes = [CFUNCTYPE(UNCHECKED(None), )]
    atexit.restype = c_int
    break

# /usr/include/stdlib.h: 603
for _lib in _libs.values():
    if not _lib.has("at_quick_exit", "cdecl"):
        continue
    at_quick_exit = _lib.get("at_quick_exit", "cdecl")
    at_quick_exit.argtypes = [CFUNCTYPE(UNCHECKED(None), )]
    at_quick_exit.restype = c_int
    break

# /usr/include/stdlib.h: 610
for _lib in _libs.values():
    if not _lib.has("on_exit", "cdecl"):
        continue
    on_exit = _lib.get("on_exit", "cdecl")
    on_exit.argtypes = [CFUNCTYPE(UNCHECKED(None), c_int, POINTER(None)), POINTER(None)]
    on_exit.restype = c_int
    break

# /usr/include/stdlib.h: 617
for _lib in _libs.values():
    if not _lib.has("exit", "cdecl"):
        continue
    exit = _lib.get("exit", "cdecl")
    exit.argtypes = [c_int]
    exit.restype = None
    break

# /usr/include/stdlib.h: 623
for _lib in _libs.values():
    if not _lib.has("quick_exit", "cdecl"):
        continue
    quick_exit = _lib.get("quick_exit", "cdecl")
    quick_exit.argtypes = [c_int]
    quick_exit.restype = None
    break

# /usr/include/stdlib.h: 629
for _lib in _libs.values():
    if not _lib.has("_Exit", "cdecl"):
        continue
    _Exit = _lib.get("_Exit", "cdecl")
    _Exit.argtypes = [c_int]
    _Exit.restype = None
    break

# /usr/include/stdlib.h: 634
for _lib in _libs.values():
    if not _lib.has("getenv", "cdecl"):
        continue
    getenv = _lib.get("getenv", "cdecl")
    getenv.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        getenv.restype = ReturnString
    else:
        getenv.restype = String
        getenv.errcheck = ReturnString
    break

# /usr/include/stdlib.h: 647
for _lib in _libs.values():
    if not _lib.has("putenv", "cdecl"):
        continue
    putenv = _lib.get("putenv", "cdecl")
    putenv.argtypes = [String]
    putenv.restype = c_int
    break

# /usr/include/stdlib.h: 653
for _lib in _libs.values():
    if not _lib.has("setenv", "cdecl"):
        continue
    setenv = _lib.get("setenv", "cdecl")
    setenv.argtypes = [String, String, c_int]
    setenv.restype = c_int
    break

# /usr/include/stdlib.h: 657
for _lib in _libs.values():
    if not _lib.has("unsetenv", "cdecl"):
        continue
    unsetenv = _lib.get("unsetenv", "cdecl")
    unsetenv.argtypes = [String]
    unsetenv.restype = c_int
    break

# /usr/include/stdlib.h: 664
for _lib in _libs.values():
    if not _lib.has("clearenv", "cdecl"):
        continue
    clearenv = _lib.get("clearenv", "cdecl")
    clearenv.argtypes = []
    clearenv.restype = c_int
    break

# /usr/include/stdlib.h: 675
for _lib in _libs.values():
    if not _lib.has("mktemp", "cdecl"):
        continue
    mktemp = _lib.get("mktemp", "cdecl")
    mktemp.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        mktemp.restype = ReturnString
    else:
        mktemp.restype = String
        mktemp.errcheck = ReturnString
    break

# /usr/include/stdlib.h: 688
for _lib in _libs.values():
    if not _lib.has("mkstemp", "cdecl"):
        continue
    mkstemp = _lib.get("mkstemp", "cdecl")
    mkstemp.argtypes = [String]
    mkstemp.restype = c_int
    break

# /usr/include/stdlib.h: 710
for _lib in _libs.values():
    if not _lib.has("mkstemps", "cdecl"):
        continue
    mkstemps = _lib.get("mkstemps", "cdecl")
    mkstemps.argtypes = [String, c_int]
    mkstemps.restype = c_int
    break

# /usr/include/stdlib.h: 731
for _lib in _libs.values():
    if not _lib.has("mkdtemp", "cdecl"):
        continue
    mkdtemp = _lib.get("mkdtemp", "cdecl")
    mkdtemp.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        mkdtemp.restype = ReturnString
    else:
        mkdtemp.restype = String
        mkdtemp.errcheck = ReturnString
    break

# /usr/include/stdlib.h: 784
for _lib in _libs.values():
    if not _lib.has("system", "cdecl"):
        continue
    system = _lib.get("system", "cdecl")
    system.argtypes = [String]
    system.restype = c_int
    break

__compar_fn_t = CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(None))# /usr/include/stdlib.h: 808

# /usr/include/stdlib.h: 820
for _lib in _libs.values():
    if not _lib.has("bsearch", "cdecl"):
        continue
    bsearch = _lib.get("bsearch", "cdecl")
    bsearch.argtypes = [POINTER(None), POINTER(None), c_size_t, c_size_t, __compar_fn_t]
    bsearch.restype = POINTER(c_ubyte)
    bsearch.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /usr/include/stdlib.h: 830
for _lib in _libs.values():
    if not _lib.has("qsort", "cdecl"):
        continue
    qsort = _lib.get("qsort", "cdecl")
    qsort.argtypes = [POINTER(None), c_size_t, c_size_t, __compar_fn_t]
    qsort.restype = None
    break

# /usr/include/stdlib.h: 840
for _lib in _libs.values():
    if not _lib.has("abs", "cdecl"):
        continue
    abs = _lib.get("abs", "cdecl")
    abs.argtypes = [c_int]
    abs.restype = c_int
    break

# /usr/include/stdlib.h: 841
for _lib in _libs.values():
    if not _lib.has("labs", "cdecl"):
        continue
    labs = _lib.get("labs", "cdecl")
    labs.argtypes = [c_long]
    labs.restype = c_long
    break

# /usr/include/stdlib.h: 844
for _lib in _libs.values():
    if not _lib.has("llabs", "cdecl"):
        continue
    llabs = _lib.get("llabs", "cdecl")
    llabs.argtypes = [c_longlong]
    llabs.restype = c_longlong
    break

# /usr/include/stdlib.h: 852
for _lib in _libs.values():
    if not _lib.has("div", "cdecl"):
        continue
    div = _lib.get("div", "cdecl")
    div.argtypes = [c_int, c_int]
    div.restype = div_t
    break

# /usr/include/stdlib.h: 854
for _lib in _libs.values():
    if not _lib.has("ldiv", "cdecl"):
        continue
    ldiv = _lib.get("ldiv", "cdecl")
    ldiv.argtypes = [c_long, c_long]
    ldiv.restype = ldiv_t
    break

# /usr/include/stdlib.h: 858
for _lib in _libs.values():
    if not _lib.has("lldiv", "cdecl"):
        continue
    lldiv = _lib.get("lldiv", "cdecl")
    lldiv.argtypes = [c_longlong, c_longlong]
    lldiv.restype = lldiv_t
    break

# /usr/include/stdlib.h: 884
for _lib in _libs.values():
    if not _lib.has("gcvt", "cdecl"):
        continue
    gcvt = _lib.get("gcvt", "cdecl")
    gcvt.argtypes = [c_double, c_int, String]
    if sizeof(c_int) == sizeof(c_void_p):
        gcvt.restype = ReturnString
    else:
        gcvt.restype = String
        gcvt.errcheck = ReturnString
    break

# /usr/include/stdlib.h: 896
for _lib in _libs.values():
    if not _lib.has("qgcvt", "cdecl"):
        continue
    qgcvt = _lib.get("qgcvt", "cdecl")
    qgcvt.argtypes = [c_longdouble, c_int, String]
    if sizeof(c_int) == sizeof(c_void_p):
        qgcvt.restype = ReturnString
    else:
        qgcvt.restype = String
        qgcvt.errcheck = ReturnString
    break

# /usr/include/stdlib.h: 922
for _lib in _libs.values():
    if not _lib.has("mblen", "cdecl"):
        continue
    mblen = _lib.get("mblen", "cdecl")
    mblen.argtypes = [String, c_size_t]
    mblen.restype = c_int
    break

# /usr/include/stdlib.h: 929
for _lib in _libs.values():
    if not _lib.has("wctomb", "cdecl"):
        continue
    wctomb = _lib.get("wctomb", "cdecl")
    wctomb.argtypes = [String, c_wchar]
    wctomb.restype = c_int
    break

# /usr/include/stdlib.h: 946
for _lib in _libs.values():
    if not _lib.has("rpmatch", "cdecl"):
        continue
    rpmatch = _lib.get("rpmatch", "cdecl")
    rpmatch.argtypes = [String]
    rpmatch.restype = c_int
    break

# /usr/include/stdlib.h: 1003
for _lib in _libs.values():
    if not _lib.has("getloadavg", "cdecl"):
        continue
    getloadavg = _lib.get("getloadavg", "cdecl")
    getloadavg.argtypes = [POINTER(c_double), c_int]
    getloadavg.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 242
for _lib in _libs.values():
    if not _lib.has("OmStartup", "cdecl"):
        continue
    OmStartup = _lib.get("OmStartup", "cdecl")
    OmStartup.argtypes = [c_int]
    OmStartup.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 253
for _lib in _libs.values():
    if not _lib.has("OmShutdown", "cdecl"):
        continue
    OmShutdown = _lib.get("OmShutdown", "cdecl")
    OmShutdown.argtypes = []
    OmShutdown.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 263
for _lib in _libs.values():
    if not _lib.has("OmSetLogStream", "cdecl"):
        continue
    OmSetLogStream = _lib.get("OmSetLogStream", "cdecl")
    OmSetLogStream.argtypes = [c_int]
    OmSetLogStream.restype = c_int
    break

OmLogCallback = CFUNCTYPE(UNCHECKED(None), POINTER(None), String)# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 273

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 283
for _lib in _libs.values():
    if not _lib.has("OmSetLogCallback", "cdecl"):
        continue
    OmSetLogCallback = _lib.get("OmSetLogCallback", "cdecl")
    OmSetLogCallback.argtypes = [OmLogCallback, POINTER(None)]
    OmSetLogCallback.restype = c_int
    break

enum_anon_20 = c_int# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 294

OM_DEVICE_REMOVED = 0# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 294

OM_DEVICE_CONNECTED = (OM_DEVICE_REMOVED + 1)# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 294

OM_DEVICE_STATUS = enum_anon_20# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 294

OmDeviceCallback = CFUNCTYPE(UNCHECKED(None), POINTER(None), c_int, OM_DEVICE_STATUS)# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 303

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 313
for _lib in _libs.values():
    if not _lib.has("OmSetDeviceCallback", "cdecl"):
        continue
    OmSetDeviceCallback = _lib.get("OmSetDeviceCallback", "cdecl")
    OmSetDeviceCallback.argtypes = [OmDeviceCallback, POINTER(None)]
    OmSetDeviceCallback.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 325
for _lib in _libs.values():
    if not _lib.has("OmGetDeviceIds", "cdecl"):
        continue
    OmGetDeviceIds = _lib.get("OmGetDeviceIds", "cdecl")
    OmGetDeviceIds.argtypes = [POINTER(c_int), c_int]
    OmGetDeviceIds.restype = c_int
    break

OM_DATETIME = c_ulong# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 335

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 370
for _lib in _libs.values():
    if not _lib.has("OmGetVersion", "cdecl"):
        continue
    OmGetVersion = _lib.get("OmGetVersion", "cdecl")
    OmGetVersion.argtypes = [c_int, POINTER(c_int), POINTER(c_int)]
    OmGetVersion.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 379
for _lib in _libs.values():
    if not _lib.has("OmGetDeviceSerial", "cdecl"):
        continue
    OmGetDeviceSerial = _lib.get("OmGetDeviceSerial", "cdecl")
    OmGetDeviceSerial.argtypes = [c_int, String]
    OmGetDeviceSerial.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 389
for _lib in _libs.values():
    if not _lib.has("OmGetDevicePort", "cdecl"):
        continue
    OmGetDevicePort = _lib.get("OmGetDevicePort", "cdecl")
    OmGetDevicePort.argtypes = [c_int, String]
    OmGetDevicePort.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 399
for _lib in _libs.values():
    if not _lib.has("OmGetDevicePath", "cdecl"):
        continue
    OmGetDevicePath = _lib.get("OmGetDevicePath", "cdecl")
    OmGetDevicePath.argtypes = [c_int, String]
    OmGetDevicePath.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 408
for _lib in _libs.values():
    if not _lib.has("OmGetBatteryLevel", "cdecl"):
        continue
    OmGetBatteryLevel = _lib.get("OmGetBatteryLevel", "cdecl")
    OmGetBatteryLevel.argtypes = [c_int]
    OmGetBatteryLevel.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 419
for _lib in _libs.values():
    if not _lib.has("OmSelfTest", "cdecl"):
        continue
    OmSelfTest = _lib.get("OmSelfTest", "cdecl")
    OmSelfTest.argtypes = [c_int]
    OmSelfTest.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 432
for _lib in _libs.values():
    if not _lib.has("OmGetMemoryHealth", "cdecl"):
        continue
    OmGetMemoryHealth = _lib.get("OmGetMemoryHealth", "cdecl")
    OmGetMemoryHealth.argtypes = [c_int]
    OmGetMemoryHealth.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 446
for _lib in _libs.values():
    if not _lib.has("OmGetBatteryHealth", "cdecl"):
        continue
    OmGetBatteryHealth = _lib.get("OmGetBatteryHealth", "cdecl")
    OmGetBatteryHealth.argtypes = [c_int]
    OmGetBatteryHealth.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 458
for _lib in _libs.values():
    if not _lib.has("OmGetAccelerometer", "cdecl"):
        continue
    OmGetAccelerometer = _lib.get("OmGetAccelerometer", "cdecl")
    OmGetAccelerometer.argtypes = [c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    OmGetAccelerometer.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 467
for _lib in _libs.values():
    if not _lib.has("OmGetTime", "cdecl"):
        continue
    OmGetTime = _lib.get("OmGetTime", "cdecl")
    OmGetTime.argtypes = [c_int, POINTER(OM_DATETIME)]
    OmGetTime.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 476
for _lib in _libs.values():
    if not _lib.has("OmSetTime", "cdecl"):
        continue
    OmSetTime = _lib.get("OmSetTime", "cdecl")
    OmSetTime.argtypes = [c_int, OM_DATETIME]
    OmSetTime.restype = c_int
    break

enum_anon_21 = c_int# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 498

OM_LED_AUTO = (-1)# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 498

OM_LED_OFF = 0# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 498

OM_LED_BLUE = 1# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 498

OM_LED_GREEN = 2# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 498

OM_LED_CYAN = 3# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 498

OM_LED_RED = 4# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 498

OM_LED_MAGENTA = 5# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 498

OM_LED_YELLOW = 6# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 498

OM_LED_WHITE = 7# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 498

OM_LED_STATE = enum_anon_21# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 498

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 508
for _lib in _libs.values():
    if not _lib.has("OmSetLed", "cdecl"):
        continue
    OmSetLed = _lib.get("OmSetLed", "cdecl")
    OmSetLed.argtypes = [c_int, OM_LED_STATE]
    OmSetLed.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 518
for _lib in _libs.values():
    if not _lib.has("OmIsLocked", "cdecl"):
        continue
    OmIsLocked = _lib.get("OmIsLocked", "cdecl")
    OmIsLocked.argtypes = [c_int, POINTER(c_int)]
    OmIsLocked.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 529
for _lib in _libs.values():
    if not _lib.has("OmSetLock", "cdecl"):
        continue
    OmSetLock = _lib.get("OmSetLock", "cdecl")
    OmSetLock.argtypes = [c_int, c_ushort]
    OmSetLock.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 540
for _lib in _libs.values():
    if not _lib.has("OmUnlock", "cdecl"):
        continue
    OmUnlock = _lib.get("OmUnlock", "cdecl")
    OmUnlock.argtypes = [c_int, c_ushort]
    OmUnlock.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 550
for _lib in _libs.values():
    if not _lib.has("OmSetEcc", "cdecl"):
        continue
    OmSetEcc = _lib.get("OmSetEcc", "cdecl")
    OmSetEcc.argtypes = [c_int, c_int]
    OmSetEcc.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 559
for _lib in _libs.values():
    if not _lib.has("OmGetEcc", "cdecl"):
        continue
    OmGetEcc = _lib.get("OmGetEcc", "cdecl")
    OmGetEcc.argtypes = [c_int]
    OmGetEcc.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 578
for _lib in _libs.values():
    if not _lib.has("OmCommand", "cdecl"):
        continue
    OmCommand = _lib.get("OmCommand", "cdecl")
    OmCommand.argtypes = [c_int, String, String, c_size_t, String, c_uint, POINTER(POINTER(c_char)), c_int]
    OmCommand.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 611
for _lib in _libs.values():
    if not _lib.has("OmGetDelays", "cdecl"):
        continue
    OmGetDelays = _lib.get("OmGetDelays", "cdecl")
    OmGetDelays.argtypes = [c_int, POINTER(OM_DATETIME), POINTER(OM_DATETIME)]
    OmGetDelays.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 629
for _lib in _libs.values():
    if not _lib.has("OmSetDelays", "cdecl"):
        continue
    OmSetDelays = _lib.get("OmSetDelays", "cdecl")
    OmSetDelays.argtypes = [c_int, OM_DATETIME, OM_DATETIME]
    OmSetDelays.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 638
for _lib in _libs.values():
    if not _lib.has("OmGetSessionId", "cdecl"):
        continue
    OmGetSessionId = _lib.get("OmGetSessionId", "cdecl")
    OmGetSessionId.argtypes = [c_int, POINTER(c_uint)]
    OmGetSessionId.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 649
for _lib in _libs.values():
    if not _lib.has("OmSetSessionId", "cdecl"):
        continue
    OmSetSessionId = _lib.get("OmSetSessionId", "cdecl")
    OmSetSessionId.argtypes = [c_int, c_uint]
    OmSetSessionId.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 666
for _lib in _libs.values():
    if not _lib.has("OmGetMetadata", "cdecl"):
        continue
    OmGetMetadata = _lib.get("OmGetMetadata", "cdecl")
    OmGetMetadata.argtypes = [c_int, String]
    OmGetMetadata.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 679
for _lib in _libs.values():
    if not _lib.has("OmSetMetadata", "cdecl"):
        continue
    OmSetMetadata = _lib.get("OmSetMetadata", "cdecl")
    OmSetMetadata.argtypes = [c_int, String, c_int]
    OmSetMetadata.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 688
for _lib in _libs.values():
    if not _lib.has("OmGetLastConfigTime", "cdecl"):
        continue
    OmGetLastConfigTime = _lib.get("OmGetLastConfigTime", "cdecl")
    OmGetLastConfigTime.argtypes = [c_int, POINTER(OM_DATETIME)]
    OmGetLastConfigTime.restype = c_int
    break

enum_anon_22 = c_int# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 702

OM_ERASE_NONE = 0# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 702

OM_ERASE_DELETE = 1# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 702

OM_ERASE_QUICKFORMAT = 2# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 702

OM_ERASE_WIPE = 3# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 702

OM_ERASE_LEVEL = enum_anon_22# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 702

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 723
for _lib in _libs.values():
    if not _lib.has("OmEraseDataAndCommit", "cdecl"):
        continue
    OmEraseDataAndCommit = _lib.get("OmEraseDataAndCommit", "cdecl")
    OmEraseDataAndCommit.argtypes = [c_int, OM_ERASE_LEVEL]
    OmEraseDataAndCommit.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 776
for _lib in _libs.values():
    if not _lib.has("OmGetAccelConfig", "cdecl"):
        continue
    OmGetAccelConfig = _lib.get("OmGetAccelConfig", "cdecl")
    OmGetAccelConfig.argtypes = [c_int, POINTER(c_int), POINTER(c_int)]
    OmGetAccelConfig.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 789
for _lib in _libs.values():
    if not _lib.has("OmSetAccelConfig", "cdecl"):
        continue
    OmSetAccelConfig = _lib.get("OmSetAccelConfig", "cdecl")
    OmSetAccelConfig.argtypes = [c_int, c_int, c_int]
    OmSetAccelConfig.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 800
for _lib in _libs.values():
    if not _lib.has("OmGetMaxSamples", "cdecl"):
        continue
    OmGetMaxSamples = _lib.get("OmGetMaxSamples", "cdecl")
    OmGetMaxSamples.argtypes = [c_int, POINTER(c_int)]
    OmGetMaxSamples.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 812
for _lib in _libs.values():
    if not _lib.has("OmSetMaxSamples", "cdecl"):
        continue
    OmSetMaxSamples = _lib.get("OmSetMaxSamples", "cdecl")
    OmSetMaxSamples.argtypes = [c_int, c_int]
    OmSetMaxSamples.restype = c_int
    break

enum_anon_23 = c_int# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 857

OM_DOWNLOAD_NONE = 0# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 857

OM_DOWNLOAD_ERROR = (OM_DOWNLOAD_NONE + 1)# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 857

OM_DOWNLOAD_PROGRESS = (OM_DOWNLOAD_ERROR + 1)# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 857

OM_DOWNLOAD_COMPLETE = (OM_DOWNLOAD_PROGRESS + 1)# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 857

OM_DOWNLOAD_CANCELLED = (OM_DOWNLOAD_COMPLETE + 1)# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 857

OM_DOWNLOAD_STATUS = enum_anon_23# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 857

OmDownloadCallback = CFUNCTYPE(UNCHECKED(None), POINTER(None), c_int, OM_DOWNLOAD_STATUS, c_int)# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 866

OmDownloadChunkCallback = CFUNCTYPE(UNCHECKED(None), POINTER(None), c_int, POINTER(None), c_int, c_int)# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 876

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 885
for _lib in _libs.values():
    if not _lib.has("OmSetDownloadCallback", "cdecl"):
        continue
    OmSetDownloadCallback = _lib.get("OmSetDownloadCallback", "cdecl")
    OmSetDownloadCallback.argtypes = [OmDownloadCallback, POINTER(None)]
    OmSetDownloadCallback.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 895
for _lib in _libs.values():
    if not _lib.has("OmSetDownloadChunkCallback", "cdecl"):
        continue
    OmSetDownloadChunkCallback = _lib.get("OmSetDownloadChunkCallback", "cdecl")
    OmSetDownloadChunkCallback.argtypes = [OmDownloadChunkCallback, POINTER(None)]
    OmSetDownloadChunkCallback.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 904
for _lib in _libs.values():
    if not _lib.has("OmGetDataFileSize", "cdecl"):
        continue
    OmGetDataFileSize = _lib.get("OmGetDataFileSize", "cdecl")
    OmGetDataFileSize.argtypes = [c_int]
    OmGetDataFileSize.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 914
for _lib in _libs.values():
    if not _lib.has("OmGetDataFilename", "cdecl"):
        continue
    OmGetDataFilename = _lib.get("OmGetDataFilename", "cdecl")
    OmGetDataFilename.argtypes = [c_int, String]
    OmGetDataFilename.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 927
for _lib in _libs.values():
    if not _lib.has("OmGetDataRange", "cdecl"):
        continue
    OmGetDataRange = _lib.get("OmGetDataRange", "cdecl")
    OmGetDataRange.argtypes = [c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(OM_DATETIME), POINTER(OM_DATETIME)]
    OmGetDataRange.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 943
for _lib in _libs.values():
    if not _lib.has("OmBeginDownloading", "cdecl"):
        continue
    OmBeginDownloading = _lib.get("OmBeginDownloading", "cdecl")
    OmBeginDownloading.argtypes = [c_int, c_int, c_int, String]
    OmBeginDownloading.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 961
for _lib in _libs.values():
    if not _lib.has("OmBeginDownloadingReference", "cdecl"):
        continue
    OmBeginDownloadingReference = _lib.get("OmBeginDownloadingReference", "cdecl")
    OmBeginDownloadingReference.argtypes = [c_int, c_int, c_int, String, POINTER(None)]
    OmBeginDownloadingReference.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 976
for _lib in _libs.values():
    if not _lib.has("OmQueryDownload", "cdecl"):
        continue
    OmQueryDownload = _lib.get("OmQueryDownload", "cdecl")
    OmQueryDownload.argtypes = [c_int, POINTER(OM_DOWNLOAD_STATUS), POINTER(c_int)]
    OmQueryDownload.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 991
for _lib in _libs.values():
    if not _lib.has("OmWaitForDownload", "cdecl"):
        continue
    OmWaitForDownload = _lib.get("OmWaitForDownload", "cdecl")
    OmWaitForDownload.argtypes = [c_int, POINTER(OM_DOWNLOAD_STATUS), POINTER(c_int)]
    OmWaitForDownload.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1001
for _lib in _libs.values():
    if not _lib.has("OmCancelDownload", "cdecl"):
        continue
    OmCancelDownload = _lib.get("OmCancelDownload", "cdecl")
    OmCancelDownload.argtypes = [c_int]
    OmCancelDownload.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1044
for _lib in _libs.values():
    if not _lib.has("OmErrorString", "cdecl"):
        continue
    OmErrorString = _lib.get("OmErrorString", "cdecl")
    OmErrorString.argtypes = [c_int]
    OmErrorString.restype = c_char_p
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1099
for _lib in _libs.values():
    if not _lib.has("OmDateTimeFromString", "cdecl"):
        continue
    OmDateTimeFromString = _lib.get("OmDateTimeFromString", "cdecl")
    OmDateTimeFromString.argtypes = [String]
    OmDateTimeFromString.restype = OM_DATETIME
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1103
for _lib in _libs.values():
    if not _lib.has("OmDateTimeToString", "cdecl"):
        continue
    OmDateTimeToString = _lib.get("OmDateTimeToString", "cdecl")
    OmDateTimeToString.argtypes = [OM_DATETIME, String]
    if sizeof(c_int) == sizeof(c_void_p):
        OmDateTimeToString.restype = ReturnString
    else:
        OmDateTimeToString.restype = String
        OmDateTimeToString.errcheck = ReturnString
    break

OmReaderHandle = POINTER(None)# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1130

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1161
for _lib in _libs.values():
    if not _lib.has("OmReaderOpen", "cdecl"):
        continue
    OmReaderOpen = _lib.get("OmReaderOpen", "cdecl")
    OmReaderOpen.argtypes = [String]
    OmReaderOpen.restype = OmReaderHandle
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1174
for _lib in _libs.values():
    if not _lib.has("OmReaderDataRange", "cdecl"):
        continue
    OmReaderDataRange = _lib.get("OmReaderDataRange", "cdecl")
    OmReaderDataRange.argtypes = [OmReaderHandle, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(OM_DATETIME), POINTER(OM_DATETIME)]
    OmReaderDataRange.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1184
for _lib in _libs.values():
    if not _lib.has("OmReaderMetadata", "cdecl"):
        continue
    OmReaderMetadata = _lib.get("OmReaderMetadata", "cdecl")
    OmReaderMetadata.argtypes = [OmReaderHandle, POINTER(c_int), POINTER(c_uint)]
    OmReaderMetadata.restype = c_char_p
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1192
for _lib in _libs.values():
    if not _lib.has("OmReaderDataBlockPosition", "cdecl"):
        continue
    OmReaderDataBlockPosition = _lib.get("OmReaderDataBlockPosition", "cdecl")
    OmReaderDataBlockPosition.argtypes = [OmReaderHandle]
    OmReaderDataBlockPosition.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1201
for _lib in _libs.values():
    if not _lib.has("OmReaderDataBlockSeek", "cdecl"):
        continue
    OmReaderDataBlockSeek = _lib.get("OmReaderDataBlockSeek", "cdecl")
    OmReaderDataBlockSeek.argtypes = [OmReaderHandle, c_int]
    OmReaderDataBlockSeek.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1213
for _lib in _libs.values():
    if not _lib.has("OmReaderNextBlock", "cdecl"):
        continue
    OmReaderNextBlock = _lib.get("OmReaderNextBlock", "cdecl")
    OmReaderNextBlock.argtypes = [OmReaderHandle]
    OmReaderNextBlock.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1225
for _lib in _libs.values():
    if not _lib.has("OmReaderBuffer", "cdecl"):
        continue
    OmReaderBuffer = _lib.get("OmReaderBuffer", "cdecl")
    OmReaderBuffer.argtypes = [OmReaderHandle]
    OmReaderBuffer.restype = POINTER(c_short)
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1240
for _lib in _libs.values():
    if not _lib.has("OmReaderTimestamp", "cdecl"):
        continue
    OmReaderTimestamp = _lib.get("OmReaderTimestamp", "cdecl")
    OmReaderTimestamp.argtypes = [OmReaderHandle, c_int, POINTER(c_ushort)]
    OmReaderTimestamp.restype = OM_DATETIME
    break

enum_anon_24 = c_int# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1275

OM_VALUE_DEVICEID = 3# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1275

OM_VALUE_SESSIONID = 4# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1275

OM_VALUE_SEQUENCEID = 5# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1275

OM_VALUE_LIGHT = 7# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1275

OM_VALUE_TEMPERATURE = 8# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1275

OM_VALUE_EVENTS = 9# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1275

OM_VALUE_BATTERY = 10# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1275

OM_VALUE_SAMPLERATE = 11# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1275

OM_VALUE_LIGHT_LOG10LUXTIMES10POWER3 = 107# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1275

OM_VALUE_TEMPERATURE_MC = 108# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1275

OM_VALUE_BATTERY_MV = 110# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1275

OM_VALUE_BATTERY_PERCENT = 210# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1275

OM_VALUE_AXES = 12# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1275

OM_VALUE_SCALE_ACCEL = 13# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1275

OM_VALUE_SCALE_GYRO = 14# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1275

OM_VALUE_SCALE_MAG = 15# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1275

OM_VALUE_ACCEL_AXIS = 16# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1275

OM_VALUE_GYRO_AXIS = 17# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1275

OM_VALUE_MAG_AXIS = 18# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1275

OM_READER_VALUE_TYPE = enum_anon_24# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1275

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1287
for _lib in _libs.values():
    if not _lib.has("OmReaderGetValue", "cdecl"):
        continue
    OmReaderGetValue = _lib.get("OmReaderGetValue", "cdecl")
    OmReaderGetValue.argtypes = [OmReaderHandle, OM_READER_VALUE_TYPE]
    OmReaderGetValue.restype = c_int
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1314
class struct_anon_25(Structure):
    pass

struct_anon_25._pack_ = 1
struct_anon_25.__slots__ = [
    'packetHeader',
    'packetLength',
    'reserved1',
    'deviceId',
    'sessionId',
    'reserved2',
    'loggingStartTime',
    'loggingEndTime',
    'loggingCapacity',
    'reserved3',
    'samplingRate',
    'lastChangeTime',
    'firmwareRevision',
    'timeZone',
    'reserved4',
    'annotation',
    'reserved',
]
struct_anon_25._fields_ = [
    ('packetHeader', c_ushort),
    ('packetLength', c_ushort),
    ('reserved1', c_ubyte),
    ('deviceId', c_ushort),
    ('sessionId', c_uint),
    ('reserved2', c_ushort),
    ('loggingStartTime', OM_DATETIME),
    ('loggingEndTime', OM_DATETIME),
    ('loggingCapacity', c_uint),
    ('reserved3', c_ubyte * int(11)),
    ('samplingRate', c_ubyte),
    ('lastChangeTime', c_uint),
    ('firmwareRevision', c_ubyte),
    ('timeZone', c_short),
    ('reserved4', c_ubyte * int(20)),
    ('annotation', c_ubyte * int(448)),
    ('reserved', c_ubyte * int(512)),
]

OM_READER_HEADER_PACKET = struct_anon_25# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1314

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1325
for _lib in _libs.values():
    if not _lib.has("OmReaderRawHeaderPacket", "cdecl"):
        continue
    OmReaderRawHeaderPacket = _lib.get("OmReaderRawHeaderPacket", "cdecl")
    OmReaderRawHeaderPacket.argtypes = [OmReaderHandle]
    OmReaderRawHeaderPacket.restype = POINTER(OM_READER_HEADER_PACKET)
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1351
class struct_anon_26(Structure):
    pass

struct_anon_26._pack_ = 1
struct_anon_26.__slots__ = [
    'packetHeader',
    'packetLength',
    'deviceFractional',
    'sessionId',
    'sequenceId',
    'timestamp',
    'light',
    'temperature',
    'events',
    'battery',
    'sampleRate',
    'numAxesBPS',
    'timestampOffset',
    'sampleCount',
    'rawSampleData',
    'checksum',
]
struct_anon_26._fields_ = [
    ('packetHeader', c_ushort),
    ('packetLength', c_ushort),
    ('deviceFractional', c_ushort),
    ('sessionId', c_uint),
    ('sequenceId', c_uint),
    ('timestamp', OM_DATETIME),
    ('light', c_ushort),
    ('temperature', c_ushort),
    ('events', c_ubyte),
    ('battery', c_ubyte),
    ('sampleRate', c_ubyte),
    ('numAxesBPS', c_ubyte),
    ('timestampOffset', c_short),
    ('sampleCount', c_ushort),
    ('rawSampleData', c_ubyte * int(480)),
    ('checksum', c_ushort),
]

OM_READER_DATA_PACKET = struct_anon_26# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1351

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1363
for _lib in _libs.values():
    if not _lib.has("OmReaderRawDataPacket", "cdecl"):
        continue
    OmReaderRawDataPacket = _lib.get("OmReaderRawDataPacket", "cdecl")
    OmReaderRawDataPacket.argtypes = [OmReaderHandle]
    OmReaderRawDataPacket.restype = POINTER(OM_READER_DATA_PACKET)
    break

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1372
for _lib in _libs.values():
    if not _lib.has("OmReaderClose", "cdecl"):
        continue
    OmReaderClose = _lib.get("OmReaderClose", "cdecl")
    OmReaderClose.argtypes = [OmReaderHandle]
    OmReaderClose.restype = None
    break

# <built-in>
try:
    __LDBL_MANT_DIG__ = 64
except:
    pass

__const = c_int# <command-line>: 4

# <command-line>: 7
try:
    CTYPESGEN = 1
except:
    pass

# /usr/include/stdc-predef.h: 19
try:
    _STDC_PREDEF_H = 1
except:
    pass

# /usr/include/stdc-predef.h: 38
try:
    __STDC_IEC_559__ = 1
except:
    pass

# /usr/include/stdc-predef.h: 46
try:
    __STDC_IEC_559_COMPLEX__ = 1
except:
    pass

# /usr/include/stdc-predef.h: 58
try:
    __STDC_ISO_10646__ = 201706.0
except:
    pass

# /usr/include/features.h: 19
try:
    _FEATURES_H = 1
except:
    pass

# /usr/include/features.h: 164
def __GNUC_PREREQ(maj, min):
    return 0

# /usr/include/features.h: 175
def __glibc_clang_prereq(maj, min):
    return 0

# /usr/include/features.h: 227
try:
    _DEFAULT_SOURCE = 1
except:
    pass

# /usr/include/features.h: 235
try:
    __GLIBC_USE_ISOC2X = 0
except:
    pass

# /usr/include/features.h: 241
try:
    __USE_ISOC11 = 1
except:
    pass

# /usr/include/features.h: 248
try:
    __USE_ISOC99 = 1
except:
    pass

# /usr/include/features.h: 255
try:
    __USE_ISOC95 = 1
except:
    pass

# /usr/include/features.h: 276
try:
    __USE_POSIX_IMPLICITLY = 1
except:
    pass

# /usr/include/features.h: 279
try:
    _POSIX_SOURCE = 1
except:
    pass

# /usr/include/features.h: 281
try:
    _POSIX_C_SOURCE = 200809.0
except:
    pass

# /usr/include/features.h: 316
try:
    __USE_POSIX = 1
except:
    pass

# /usr/include/features.h: 320
try:
    __USE_POSIX2 = 1
except:
    pass

# /usr/include/features.h: 324
try:
    __USE_POSIX199309 = 1
except:
    pass

# /usr/include/features.h: 328
try:
    __USE_POSIX199506 = 1
except:
    pass

# /usr/include/features.h: 332
try:
    __USE_XOPEN2K = 1
except:
    pass

# /usr/include/features.h: 333
# #undef __USE_ISOC95
try:
    del __USE_ISOC95
except NameError:
    pass

# /usr/include/features.h: 334
try:
    __USE_ISOC95 = 1
except:
    pass

# /usr/include/features.h: 335
# #undef __USE_ISOC99
try:
    del __USE_ISOC99
except NameError:
    pass

# /usr/include/features.h: 336
try:
    __USE_ISOC99 = 1
except:
    pass

# /usr/include/features.h: 340
try:
    __USE_XOPEN2K8 = 1
except:
    pass

# /usr/include/features.h: 342
try:
    _ATFILE_SOURCE = 1
except:
    pass

# /usr/include/features.h: 384
try:
    __USE_MISC = 1
except:
    pass

# /usr/include/features.h: 388
try:
    __USE_ATFILE = 1
except:
    pass

# /usr/include/features.h: 403
try:
    __USE_FORTIFY_LEVEL = 0
except:
    pass

# /usr/include/features.h: 411
try:
    __GLIBC_USE_DEPRECATED_GETS = 0
except:
    pass

# /usr/include/features.h: 434
try:
    __GLIBC_USE_DEPRECATED_SCANF = 0
except:
    pass

# /usr/include/features.h: 448
try:
    __GNU_LIBRARY__ = 6
except:
    pass

# /usr/include/features.h: 452
try:
    __GLIBC__ = 2
except:
    pass

# /usr/include/features.h: 453
try:
    __GLIBC_MINOR__ = 31
except:
    pass

# /usr/include/features.h: 455
def __GLIBC_PREREQ(maj, min):
    return (((__GLIBC__ << 16) + __GLIBC_MINOR__) >= ((maj << 16) + min))

# /usr/include/x86_64-linux-gnu/sys/cdefs.h: 19
try:
    _SYS_CDEFS_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/cdefs.h: 84
def __NTH(fct):
    return fct

# /usr/include/x86_64-linux-gnu/sys/cdefs.h: 94
def __glibc_clang_has_extension(ext):
    return 0

# /usr/include/x86_64-linux-gnu/sys/cdefs.h: 99
def __P(args):
    return args

# /usr/include/x86_64-linux-gnu/sys/cdefs.h: 100
def __PMT(args):
    return args

# /usr/include/x86_64-linux-gnu/sys/cdefs.h: 106
def __STRING(x):
    return x

__ptr_t = POINTER(None)# /usr/include/x86_64-linux-gnu/sys/cdefs.h: 109

# /usr/include/x86_64-linux-gnu/sys/cdefs.h: 144
try:
    __glibc_c99_flexarr_available = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/cdefs.h: 405
def __glibc_unlikely(cond):
    return cond

# /usr/include/x86_64-linux-gnu/sys/cdefs.h: 406
def __glibc_likely(cond):
    return cond

# /usr/include/x86_64-linux-gnu/bits/wordsize.h: 4
try:
    __WORDSIZE = 64
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/wordsize.h: 12
try:
    __WORDSIZE_TIME64_COMPAT32 = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/wordsize.h: 14
try:
    __SYSCALL_WORDSIZE = 64
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/long-double.h: 21
try:
    __LONG_DOUBLE_USES_FLOAT128 = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/cdefs.h: 475
def __LDBL_REDIR1(name, proto, alias):
    return (name + proto)

# /usr/include/x86_64-linux-gnu/sys/cdefs.h: 476
def __LDBL_REDIR(name, proto):
    return (name + proto)

# /usr/include/x86_64-linux-gnu/sys/cdefs.h: 512
try:
    __HAVE_GENERIC_SELECTION = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/libc-header-start.h: 42
try:
    __GLIBC_USE_LIB_EXT2 = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/libc-header-start.h: 53
try:
    __GLIBC_USE_IEC_60559_BFP_EXT = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/libc-header-start.h: 59
try:
    __GLIBC_USE_IEC_60559_BFP_EXT_C2X = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/libc-header-start.h: 70
try:
    __GLIBC_USE_IEC_60559_FUNCS_EXT = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/libc-header-start.h: 76
try:
    __GLIBC_USE_IEC_60559_FUNCS_EXT_C2X = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/libc-header-start.h: 85
try:
    __GLIBC_USE_IEC_60559_TYPES_EXT = 0
except:
    pass

# /usr/include/stdlib.h: 35
try:
    _STDLIB_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/waitflags.h: 25
try:
    WNOHANG = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/waitflags.h: 26
try:
    WUNTRACED = 2
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/waitflags.h: 30
try:
    WSTOPPED = 2
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/waitflags.h: 31
try:
    WEXITED = 4
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/waitflags.h: 32
try:
    WCONTINUED = 8
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/waitflags.h: 33
try:
    WNOWAIT = 16777216
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/waitflags.h: 36
try:
    __WNOTHREAD = 536870912
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/waitflags.h: 38
try:
    __WALL = 1073741824
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/waitflags.h: 39
try:
    __WCLONE = 2147483648
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/waitflags.h: 44
try:
    __ENUM_IDTYPE_T = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/waitstatus.h: 28
def __WEXITSTATUS(status):
    return ((status & 65280) >> 8)

# /usr/include/x86_64-linux-gnu/bits/waitstatus.h: 31
def __WTERMSIG(status):
    return (status & 127)

# /usr/include/x86_64-linux-gnu/bits/waitstatus.h: 34
def __WSTOPSIG(status):
    return (__WEXITSTATUS (status))

# /usr/include/x86_64-linux-gnu/bits/waitstatus.h: 37
def __WIFEXITED(status):
    return ((__WTERMSIG (status)) == 0)

# /usr/include/x86_64-linux-gnu/bits/waitstatus.h: 40
def __WIFSIGNALED(status):
    return (((c_char ((((status & 127) + 1)))).value >> 1) > 0)

# /usr/include/x86_64-linux-gnu/bits/waitstatus.h: 44
def __WIFSTOPPED(status):
    return ((status & 255) == 127)

# /usr/include/x86_64-linux-gnu/bits/waitstatus.h: 49
def __WIFCONTINUED(status):
    return (status == __W_CONTINUED)

# /usr/include/x86_64-linux-gnu/bits/waitstatus.h: 53
def __WCOREDUMP(status):
    return (status & __WCOREFLAG)

# /usr/include/x86_64-linux-gnu/bits/waitstatus.h: 56
def __W_EXITCODE(ret, sig):
    return ((ret << 8) | sig)

# /usr/include/x86_64-linux-gnu/bits/waitstatus.h: 57
def __W_STOPCODE(sig):
    return ((sig << 8) | 127)

# /usr/include/x86_64-linux-gnu/bits/waitstatus.h: 58
try:
    __W_CONTINUED = 65535
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/waitstatus.h: 59
try:
    __WCOREFLAG = 128
except:
    pass

# /usr/include/stdlib.h: 43
def WEXITSTATUS(status):
    return (__WEXITSTATUS (status))

# /usr/include/stdlib.h: 44
def WTERMSIG(status):
    return (__WTERMSIG (status))

# /usr/include/stdlib.h: 45
def WSTOPSIG(status):
    return (__WSTOPSIG (status))

# /usr/include/stdlib.h: 46
def WIFEXITED(status):
    return (__WIFEXITED (status))

# /usr/include/stdlib.h: 47
def WIFSIGNALED(status):
    return (__WIFSIGNALED (status))

# /usr/include/stdlib.h: 48
def WIFSTOPPED(status):
    return (__WIFSTOPPED (status))

# /usr/include/stdlib.h: 50
def WIFCONTINUED(status):
    return (__WIFCONTINUED (status))

# /usr/include/x86_64-linux-gnu/bits/floatn.h: 35
try:
    __HAVE_FLOAT128 = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/floatn.h: 43
try:
    __HAVE_DISTINCT_FLOAT128 = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/floatn.h: 49
try:
    __HAVE_FLOAT64X = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/floatn.h: 55
try:
    __HAVE_FLOAT64X_LONG_DOUBLE = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/long-double.h: 21
try:
    __LONG_DOUBLE_USES_FLOAT128 = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/floatn-common.h: 34
try:
    __HAVE_FLOAT16 = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/floatn-common.h: 35
try:
    __HAVE_FLOAT32 = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/floatn-common.h: 36
try:
    __HAVE_FLOAT64 = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/floatn-common.h: 37
try:
    __HAVE_FLOAT32X = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/floatn-common.h: 38
try:
    __HAVE_FLOAT128X = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/floatn-common.h: 52
try:
    __HAVE_DISTINCT_FLOAT16 = __HAVE_FLOAT16
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/floatn-common.h: 53
try:
    __HAVE_DISTINCT_FLOAT32 = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/floatn-common.h: 54
try:
    __HAVE_DISTINCT_FLOAT64 = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/floatn-common.h: 55
try:
    __HAVE_DISTINCT_FLOAT32X = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/floatn-common.h: 56
try:
    __HAVE_DISTINCT_FLOAT64X = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/floatn-common.h: 57
try:
    __HAVE_DISTINCT_FLOAT128X = __HAVE_FLOAT128X
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/floatn-common.h: 63
try:
    __HAVE_FLOAT128_UNLIKE_LDBL = (__HAVE_DISTINCT_FLOAT128 and (__LDBL_MANT_DIG__ != 113))
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/floatn-common.h: 72
try:
    __HAVE_FLOATN_NOT_TYPEDEF = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/floatn-common.h: 102
def __f64(x):
    return x

# /usr/include/x86_64-linux-gnu/bits/floatn-common.h: 111
def __f32x(x):
    return x

# /usr/include/stdlib.h: 71
try:
    __ldiv_t_defined = 1
except:
    pass

# /usr/include/stdlib.h: 81
try:
    __lldiv_t_defined = 1
except:
    pass

# /usr/include/stdlib.h: 86
try:
    RAND_MAX = 2147483647
except:
    pass

# /usr/include/stdlib.h: 91
try:
    EXIT_FAILURE = 1
except:
    pass

# /usr/include/stdlib.h: 92
try:
    EXIT_SUCCESS = 0
except:
    pass

# /usr/include/stdlib.h: 96
try:
    MB_CUR_MAX = (__ctype_get_mb_cur_max ())
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/types.h: 23
try:
    _SYS_TYPES_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/types.h: 24
try:
    _BITS_TYPES_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/wordsize.h: 4
try:
    __WORDSIZE = 64
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/wordsize.h: 12
try:
    __WORDSIZE_TIME64_COMPAT32 = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/wordsize.h: 14
try:
    __SYSCALL_WORDSIZE = 64
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timesize.h: 24
try:
    __TIMESIZE = __WORDSIZE
except:
    pass

__S16_TYPE = c_int# /usr/include/x86_64-linux-gnu/bits/types.h: 109

__U16_TYPE = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 110

__S32_TYPE = c_int# /usr/include/x86_64-linux-gnu/bits/types.h: 111

__U32_TYPE = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 112

__SLONGWORD_TYPE = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 113

__ULONGWORD_TYPE = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 114

__SQUAD_TYPE = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 128

__UQUAD_TYPE = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 129

__SWORD_TYPE = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 130

__UWORD_TYPE = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 131

__SLONG32_TYPE = c_int# /usr/include/x86_64-linux-gnu/bits/types.h: 132

__ULONG32_TYPE = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 133

__S64_TYPE = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 134

__U64_TYPE = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 135

# /usr/include/x86_64-linux-gnu/bits/typesizes.h: 24
try:
    _BITS_TYPESIZES_H = 1
except:
    pass

__TIMER_T_TYPE = POINTER(None)# /usr/include/x86_64-linux-gnu/bits/typesizes.h: 70

# /usr/include/x86_64-linux-gnu/bits/typesizes.h: 72
class struct_anon_27(Structure):
    pass

struct_anon_27.__slots__ = [
    '__val',
]
struct_anon_27._fields_ = [
    ('__val', c_int * int(2)),
]

__FSID_T_TYPE = struct_anon_27# /usr/include/x86_64-linux-gnu/bits/typesizes.h: 72

# /usr/include/x86_64-linux-gnu/bits/typesizes.h: 80
try:
    __OFF_T_MATCHES_OFF64_T = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/typesizes.h: 83
try:
    __INO_T_MATCHES_INO64_T = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/typesizes.h: 86
try:
    __RLIM_T_MATCHES_RLIM64_T = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/typesizes.h: 89
try:
    __STATFS_MATCHES_STATFS64 = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/typesizes.h: 97
try:
    __FD_SETSIZE = 1024
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/time64.h: 24
try:
    _BITS_TIME64_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/types/clock_t.h: 2
try:
    __clock_t_defined = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/types/clockid_t.h: 2
try:
    __clockid_t_defined = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/types/time_t.h: 2
try:
    __time_t_defined = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/types/timer_t.h: 2
try:
    __timer_t_defined = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/stdint-intn.h: 20
try:
    _BITS_STDINT_INTN_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/types.h: 171
try:
    __BIT_TYPES_DEFINED__ = 1
except:
    pass

# /usr/include/endian.h: 19
try:
    _ENDIAN_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/endian.h: 20
try:
    _BITS_ENDIAN_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/endian.h: 30
try:
    __LITTLE_ENDIAN = 1234
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/endian.h: 31
try:
    __BIG_ENDIAN = 4321
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/endian.h: 32
try:
    __PDP_ENDIAN = 3412
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/endianness.h: 2
try:
    _BITS_ENDIANNESS_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/endianness.h: 9
try:
    __BYTE_ORDER = __LITTLE_ENDIAN
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/endian.h: 40
try:
    __FLOAT_WORD_ORDER = __BYTE_ORDER
except:
    pass

# /usr/include/endian.h: 27
try:
    LITTLE_ENDIAN = __LITTLE_ENDIAN
except:
    pass

# /usr/include/endian.h: 28
try:
    BIG_ENDIAN = __BIG_ENDIAN
except:
    pass

# /usr/include/endian.h: 29
try:
    PDP_ENDIAN = __PDP_ENDIAN
except:
    pass

# /usr/include/endian.h: 30
try:
    BYTE_ORDER = __BYTE_ORDER
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/byteswap.h: 24
try:
    _BITS_BYTESWAP_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/byteswap.h: 30
def __bswap_constant_16(x):
    return (__uint16_t (ord_if_char((((x >> 8) & 255) | ((x & 255) << 8))))).value

# /usr/include/x86_64-linux-gnu/bits/byteswap.h: 44
def __bswap_constant_32(x):
    return (((((x & 4278190080) >> 24) | ((x & 16711680) >> 8)) | ((x & 65280) << 8)) | ((x & 255) << 24))

# /usr/include/x86_64-linux-gnu/bits/byteswap.h: 59
def __bswap_constant_64(x):
    return (((((((((x & 18374686479671623680) >> 56) | ((x & 71776119061217280) >> 40)) | ((x & 280375465082880) >> 24)) | ((x & 1095216660480) >> 8)) | ((x & 4278190080) << 8)) | ((x & 16711680) << 24)) | ((x & 65280) << 40)) | ((x & 255) << 56))

# /usr/include/x86_64-linux-gnu/bits/uintn-identity.h: 24
try:
    _BITS_UINTN_IDENTITY_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/select.h: 22
try:
    _SYS_SELECT_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/wordsize.h: 4
try:
    __WORDSIZE = 64
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/wordsize.h: 12
try:
    __WORDSIZE_TIME64_COMPAT32 = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/wordsize.h: 14
try:
    __SYSCALL_WORDSIZE = 64
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/select.h: 58
def __FD_SET(d, set):
    return None

# /usr/include/x86_64-linux-gnu/bits/select.h: 60
def __FD_CLR(d, set):
    return None

# /usr/include/x86_64-linux-gnu/bits/select.h: 62
def __FD_ISSET(d, set):
    return ((((__FDS_BITS (set)) [(__FD_ELT (d))]) & (__FD_MASK (d))) != 0)

# /usr/include/x86_64-linux-gnu/bits/types/sigset_t.h: 2
try:
    __sigset_t_defined = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/types/__sigset_t.h: 4
try:
    _SIGSET_NWORDS = (1024 / (8 * sizeof(c_ulong)))
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/types/struct_timeval.h: 2
try:
    __timeval_defined = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/types/struct_timespec.h: 3
try:
    _STRUCT_TIMESPEC = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/select.h: 54
try:
    __NFDBITS = (8 * (c_int (ord_if_char(sizeof(__fd_mask)))).value)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/select.h: 55
def __FD_ELT(d):
    return (d / __NFDBITS)

# /usr/include/x86_64-linux-gnu/sys/select.h: 56
def __FD_MASK(d):
    return (__fd_mask (ord_if_char((1 << (d % __NFDBITS))))).value

# /usr/include/x86_64-linux-gnu/sys/select.h: 68
def __FDS_BITS(set):
    return (set.contents.__fds_bits)

# /usr/include/x86_64-linux-gnu/sys/select.h: 73
try:
    FD_SETSIZE = __FD_SETSIZE
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/select.h: 80
try:
    NFDBITS = __NFDBITS
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/select.h: 85
def FD_SET(fd, fdsetp):
    return (__FD_SET (fd, fdsetp))

# /usr/include/x86_64-linux-gnu/sys/select.h: 86
def FD_CLR(fd, fdsetp):
    return (__FD_CLR (fd, fdsetp))

# /usr/include/x86_64-linux-gnu/sys/select.h: 87
def FD_ISSET(fd, fdsetp):
    return (__FD_ISSET (fd, fdsetp))

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 20
try:
    _BITS_PTHREADTYPES_COMMON_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/thread-shared-types.h: 20
try:
    _THREAD_SHARED_TYPES_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes-arch.h: 19
try:
    _BITS_PTHREADTYPES_ARCH_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/wordsize.h: 4
try:
    __WORDSIZE = 64
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/wordsize.h: 12
try:
    __WORDSIZE_TIME64_COMPAT32 = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/wordsize.h: 14
try:
    __SYSCALL_WORDSIZE = 64
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes-arch.h: 25
try:
    __SIZEOF_PTHREAD_MUTEX_T = 40
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes-arch.h: 26
try:
    __SIZEOF_PTHREAD_ATTR_T = 56
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes-arch.h: 27
try:
    __SIZEOF_PTHREAD_RWLOCK_T = 56
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes-arch.h: 28
try:
    __SIZEOF_PTHREAD_BARRIER_T = 32
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes-arch.h: 41
try:
    __SIZEOF_PTHREAD_MUTEXATTR_T = 4
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes-arch.h: 42
try:
    __SIZEOF_PTHREAD_COND_T = 48
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes-arch.h: 43
try:
    __SIZEOF_PTHREAD_CONDATTR_T = 4
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes-arch.h: 44
try:
    __SIZEOF_PTHREAD_RWLOCKATTR_T = 8
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes-arch.h: 45
try:
    __SIZEOF_PTHREAD_BARRIERATTR_T = 4
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/struct_mutex.h: 20
try:
    _THREAD_MUTEX_INTERNAL_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/struct_mutex.h: 37
try:
    __PTHREAD_MUTEX_HAVE_PREV = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 63
try:
    __have_pthread_attr_t = 1
except:
    pass

# /usr/include/alloca.h: 19
try:
    _ALLOCA_H = 1
except:
    pass

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 228
try:
    OM_VERSION = 108
except:
    pass

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 434
try:
    OM_MEMORY_HEALTH_ERROR = 1
except:
    pass

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 435
try:
    OM_MEMORY_HEALTH_WARNING = 8
except:
    pass

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 656
try:
    OM_METADATA_SIZE = 448
except:
    pass

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 735
def OmClearDataAndCommit(_deviceId):
    return (OmEraseDataAndCommit (_deviceId, OM_ERASE_QUICKFORMAT))

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 748
def OmCommit(_deviceId):
    return (OmEraseDataAndCommit (_deviceId, OM_ERASE_NONE))

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 756
try:
    OM_ACCEL_DEFAULT_RATE = 100
except:
    pass

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 764
try:
    OM_ACCEL_DEFAULT_RANGE = 8
except:
    pass

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 843
try:
    OM_MAX_PATH = 256
except:
    pass

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1020
try:
    OM_TRUE = 1
except:
    pass

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1021
try:
    OM_FALSE = 0
except:
    pass

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1022
try:
    OM_OK = 0
except:
    pass

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1023
try:
    OM_E_FAIL = (-1)
except:
    pass

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1024
try:
    OM_E_UNEXPECTED = (-2)
except:
    pass

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1025
try:
    OM_E_NOT_VALID_STATE = (-3)
except:
    pass

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1026
try:
    OM_E_OUT_OF_MEMORY = (-4)
except:
    pass

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1027
try:
    OM_E_INVALID_ARG = (-5)
except:
    pass

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1028
try:
    OM_E_POINTER = (-6)
except:
    pass

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1029
try:
    OM_E_NOT_IMPLEMENTED = (-7)
except:
    pass

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1030
try:
    OM_E_ABORT = (-8)
except:
    pass

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1031
try:
    OM_E_ACCESS_DENIED = (-9)
except:
    pass

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1032
try:
    OM_E_INVALID_DEVICE = (-10)
except:
    pass

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1033
try:
    OM_E_UNEXPECTED_RESPONSE = (-11)
except:
    pass

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1034
try:
    OM_E_LOCKED = (-12)
except:
    pass

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1035
def OM_SUCCEEDED(value):
    return (value >= 0)

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1036
def OM_FAILED(value):
    return (value < 0)

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1076
def OM_DATETIME_FROM_YMDHMS(year, month, day, hours, minutes, seconds):
    return ((((((((OM_DATETIME (ord_if_char((year % 100)))).value & 63) << 26) | (((OM_DATETIME (ord_if_char(month))).value & 15) << 22)) | (((OM_DATETIME (ord_if_char(day))).value & 31) << 17)) | (((OM_DATETIME (ord_if_char(hours))).value & 31) << 12)) | (((OM_DATETIME (ord_if_char(minutes))).value & 63) << 6)) | ((OM_DATETIME (ord_if_char(seconds))).value & 63))

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1084
def OM_DATETIME_YEAR(dateTime):
    return ((c_uint (ord_if_char((c_ubyte (ord_if_char(((dateTime >> 26) & 63)))).value))).value + 2000)

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1085
def OM_DATETIME_MONTH(dateTime):
    return (c_ubyte (ord_if_char(((dateTime >> 22) & 15)))).value

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1086
def OM_DATETIME_DAY(dateTime):
    return (c_ubyte (ord_if_char(((dateTime >> 17) & 31)))).value

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1087
def OM_DATETIME_HOURS(dateTime):
    return (c_ubyte (ord_if_char(((dateTime >> 12) & 31)))).value

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1088
def OM_DATETIME_MINUTES(dateTime):
    return (c_ubyte (ord_if_char(((dateTime >> 6) & 63)))).value

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1089
def OM_DATETIME_SECONDS(dateTime):
    return (c_ubyte (ord_if_char((dateTime & 63)))).value

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1090
try:
    OM_DATETIME_MIN_VALID = (OM_DATETIME_FROM_YMDHMS (2000, 1, 1, 0, 0, 0))
except:
    pass

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1091
try:
    OM_DATETIME_MAX_VALID = (OM_DATETIME_FROM_YMDHMS (2063, 12, 31, 23, 59, 59))
except:
    pass

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1092
try:
    OM_DATETIME_ZERO = 0
except:
    pass

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1093
try:
    OM_DATETIME_INFINITE = (OM_DATETIME (ord_if_char((-1)))).value
except:
    pass

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1096
try:
    OM_DATETIME_BUFFER_SIZE = 20
except:
    pass

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1137
try:
    OM_MAX_SAMPLES = 120
except:
    pass

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1144
try:
    OM_MAX_HEADER_SIZE = (2 * 512)
except:
    pass

# /mnt/d/Newcastle/Projects/libomapi/include/omapi.h: 1151
try:
    OM_MAX_DATA_SIZE = 512
except:
    pass

timeval = struct_timeval# /usr/include/x86_64-linux-gnu/bits/types/struct_timeval.h: 8

timespec = struct_timespec# /usr/include/x86_64-linux-gnu/bits/types/struct_timespec.h: 10

__pthread_internal_list = struct___pthread_internal_list# /usr/include/x86_64-linux-gnu/bits/thread-shared-types.h: 49

__pthread_internal_slist = struct___pthread_internal_slist# /usr/include/x86_64-linux-gnu/bits/thread-shared-types.h: 55

__pthread_mutex_s = struct___pthread_mutex_s# /usr/include/x86_64-linux-gnu/bits/struct_mutex.h: 22

__pthread_rwlock_arch_t = struct___pthread_rwlock_arch_t# /usr/include/x86_64-linux-gnu/bits/struct_rwlock.h: 23

__pthread_cond_s = struct___pthread_cond_s# /usr/include/x86_64-linux-gnu/bits/thread-shared-types.h: 92

pthread_attr_t = union_pthread_attr_t# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 56

random_data = struct_random_data# /usr/include/stdlib.h: 423

drand48_data = struct_drand48_data# /usr/include/stdlib.h: 490

# No inserted files

# No prefix-stripping

