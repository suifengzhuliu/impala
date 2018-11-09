#
# Autogenerated by Thrift Compiler (0.9.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class TLogLevel:
  VLOG_3 = 0
  VLOG_2 = 1
  VLOG = 2
  INFO = 3
  WARN = 4
  ERROR = 5
  FATAL = 6

  _VALUES_TO_NAMES = {
    0: "VLOG_3",
    1: "VLOG_2",
    2: "VLOG",
    3: "INFO",
    4: "WARN",
    5: "ERROR",
    6: "FATAL",
  }

  _NAMES_TO_VALUES = {
    "VLOG_3": 0,
    "VLOG_2": 1,
    "VLOG": 2,
    "INFO": 3,
    "WARN": 4,
    "ERROR": 5,
    "FATAL": 6,
  }


class TGetJavaLogLevelParams:
  """
  Attributes:
   - class_name
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'class_name', None, None, ), # 1
  )

  def __init__(self, class_name=None,):
    self.class_name = class_name

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.class_name = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TGetJavaLogLevelParams')
    if self.class_name is not None:
      oprot.writeFieldBegin('class_name', TType.STRING, 1)
      oprot.writeString(self.class_name)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.class_name is None:
      raise TProtocol.TProtocolException(message='Required field class_name is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TSetJavaLogLevelParams:
  """
  Attributes:
   - class_name
   - log_level
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'class_name', None, None, ), # 1
    (2, TType.STRING, 'log_level', None, None, ), # 2
  )

  def __init__(self, class_name=None, log_level=None,):
    self.class_name = class_name
    self.log_level = log_level

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.class_name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.log_level = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TSetJavaLogLevelParams')
    if self.class_name is not None:
      oprot.writeFieldBegin('class_name', TType.STRING, 1)
      oprot.writeString(self.class_name)
      oprot.writeFieldEnd()
    if self.log_level is not None:
      oprot.writeFieldBegin('log_level', TType.STRING, 2)
      oprot.writeString(self.log_level)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.class_name is None:
      raise TProtocol.TProtocolException(message='Required field class_name is unset!')
    if self.log_level is None:
      raise TProtocol.TProtocolException(message='Required field log_level is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)