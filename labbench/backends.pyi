from labbench.backends import *
import labbench
import builtins

class CommandLineWrapper(labbench.core.Device):
    @Bool(help=' are we connected? ')
    def connected(self) -> None: ...
    def connected(func) -> None: ...
    def __imports__(self) -> None: ...
    def open(self) -> None: ...
    def foreground(self, *extra_arguments, **flags) -> None: ...
    def background(self, *extra_arguments, **flags) -> None: ...
    def _CommandLineWrapper__make_commandline(self, *extra_arguments, **flags) -> None: ...
    def read_stdout(self, wait_for=0) -> None: ...
    def write_stdin(self, text) -> None: ...
    def kill(self) -> None: ...
    def running(self) -> None: ...
    def clear(self) -> None: ...
    def close(self) -> None: ...
    def __init__(self, resource: str = '', *, concurrency_support: bool = True, binary_path: str = <class 'labbench.core.Undefined'>, timeout: float = 1, arguments: list = [], arguments_min: int = 0) -> None: ...
    def __init_wrapped__(self, **settings) -> None: ...
    pass

class DotNetDevice(labbench.core.Device):
    @Bool(help=' are we connected? ')
    def connected(self) -> None: ...
    def connected(func) -> None: ...
    def __imports__(self) -> None: ...
    def open(self) -> None: ...
    def __init__(self, resource: str = '', *, concurrency_support: bool = True) -> None: ...
    def __init_wrapped__(self, **settings) -> None: ...
    pass

class LabviewSocketInterface(labbench.core.Device):
    @Bool(help=' are we connected? ')
    def connected(self) -> None: ...
    def connected(func) -> None: ...
    def open(self) -> None: ...
    def close(self) -> None: ...
    def write(self, msg) -> None: ...
    def __command_set__(self, name, command, value) -> None: ...
    def read(self, convert_func=None) -> None: ...
    def clear(self) -> None: ...
    def __init__(self, resource: str = '127.0.0.1', *, concurrency_support: bool = True, tx_port: int = 61551, rx_port: int = 61552, delay: float = 1, timeout: float = 2, rx_buffer_size: int = 1024) -> None: ...
    def __init_wrapped__(self, **settings) -> None: ...
    pass

class SerialDevice(labbench.core.Device):
    @Bool(help=' are we connected? ')
    def connected(self) -> None: ...
    def connected(func) -> None: ...
    def __imports__(self) -> None: ...
    def open(self) -> None: ...
    def close(self) -> None: ...
    def __init__(self, resource: str = '', *, concurrency_support: bool = True, timeout: float = 2, write_termination: bytes = b'\n', baud_rate: int = 9600, parity: bytes = b'N', stopbits: float = 1, xonxoff: bool = False, rtscts: bool = False, dsrdtr: bool = False) -> None: ...
    def __init_wrapped__(self, **settings) -> None: ...
    pass

class SerialLoggingDevice(labbench.backends.SerialDevice):
    @Bool(help=' are we connected? ')
    def connected(self) -> None: ...
    def connected(func) -> None: ...
    def configure(self) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def running(self) -> None: ...
    def fetch(self) -> None: ...
    def clear(self) -> None: ...
    def close(self) -> None: ...
    def __init__(self, resource: str = '', *, concurrency_support: bool = True, timeout: float = 2, write_termination: bytes = b'\n', baud_rate: int = 9600, parity: bytes = b'N', stopbits: float = 1, xonxoff: bool = False, rtscts: bool = False, dsrdtr: bool = False, poll_rate: float = 0.1, data_format: bytes = b'', stop_timeout: float = 0.5, max_queue_size: int = 100000) -> None: ...
    def __init_wrapped__(self, **settings) -> None: ...
    pass

class TelnetDevice(labbench.core.Device):
    @Bool(help=' are we connected? ')
    def connected(self) -> None: ...
    def connected(func) -> None: ...
    def __imports__(self) -> None: ...
    def open(self) -> None: ...
    def close(self) -> None: ...
    def __init__(self, resource: str = '', *, concurrency_support: bool = True, timeout: float = 2, port: int = 23) -> None: ...
    def __init_wrapped__(self, **settings) -> None: ...
    pass

class VISADevice(labbench.core.Device):
    @Bool(help=' are we connected? ')
    def connected(self) -> None: ...
    def connected(func) -> None: ...
    def identity(func) -> None: ...
    def options(func) -> None: ...
    @Dict(command='*STB',help=' VISA status byte reported by the instrument ',settable=False)
    def status_byte(self) -> None: ...
    def status_byte(func) -> None: ...
    def _VISADevice__release_remote_control(self) -> None: ...
    def open(self) -> None: ...
    def close(self) -> None: ...
    def write(self, msg) -> None: ...
    def query(self, msg, timeout=None) -> None: ...
    def __command_get__(self, name, command) -> None: ...
    def __command_set__(self, name, command, value) -> None: ...
    def wait(self) -> None: ...
    def preset(self) -> None: ...
    def overlap_and_block(self, timeout=None, quiet=False) -> None: ...
    def __init__(self, resource: str = '', *, concurrency_support: bool = True, read_termination: str = '\n', write_termination: str = '\n') -> None: ...
    def __init_wrapped__(self, **settings) -> None: ...
    pass

class EmulatedVISADevice(labbench.core.Device):
    @Bool(help=' are we connected? ')
    def connected(self) -> None: ...
    def connected(func) -> None: ...
    @Unicode(command='*IDN',help=' identity string reported by the instrument ',settable=False,cache=True)
    def identity(self) -> None: ...
    def identity(func) -> None: ...
    @Unicode(command='*OPT',help=' options reported by the instrument ',settable=False,cache=True)
    def options(self) -> None: ...
    def options(func) -> None: ...
    @Dict(command='*STB',help=' VISA status byte reported by the instrument ',settable=False)
    def status_byte(self) -> None: ...
    def status_byte(func) -> None: ...
    def __command_get__(self, name, command) -> None: ...
    def __command_set__(self, name, command, value) -> None: ...
    def __init__(self, resource: str = '', *, concurrency_support: bool = True, read_termination: str = '\n', write_termination: str = '\n') -> None: ...
    def __init_wrapped__(self, **settings) -> None: ...
    pass

class Win32ComDevice(labbench.core.Device):
    @Bool(help=' are we connected? ')
    def connected(self) -> None: ...
    def connected(func) -> None: ...
    def __imports__(self) -> None: ...
    def open(self) -> None: ...
    def close(self) -> None: ...
    def __init__(self, resource: str = '', *, concurrency_support: bool = True, com_object: str = '') -> None: ...
    def __init_wrapped__(self, **settings) -> None: ...
    pass

