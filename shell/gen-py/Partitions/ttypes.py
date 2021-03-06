#
# Autogenerated by Thrift Compiler (0.9.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import Exprs.ttypes


from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class TPartitionType:
  UNPARTITIONED = 0
  RANDOM = 1
  HASH_PARTITIONED = 2
  RANGE_PARTITIONED = 3
  KUDU = 4

  _VALUES_TO_NAMES = {
    0: "UNPARTITIONED",
    1: "RANDOM",
    2: "HASH_PARTITIONED",
    3: "RANGE_PARTITIONED",
    4: "KUDU",
  }

  _NAMES_TO_VALUES = {
    "UNPARTITIONED": 0,
    "RANDOM": 1,
    "HASH_PARTITIONED": 2,
    "RANGE_PARTITIONED": 3,
    "KUDU": 4,
  }


class TDataPartition:
  """
  Attributes:
   - type
   - partition_exprs
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'type', None, None, ), # 1
    (2, TType.LIST, 'partition_exprs', (TType.STRUCT,(Exprs.ttypes.TExpr, Exprs.ttypes.TExpr.thrift_spec)), None, ), # 2
  )

  def __init__(self, type=None, partition_exprs=None,):
    self.type = type
    self.partition_exprs = partition_exprs

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
        if ftype == TType.I32:
          self.type = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.partition_exprs = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = Exprs.ttypes.TExpr()
            _elem5.read(iprot)
            self.partition_exprs.append(_elem5)
          iprot.readListEnd()
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
    oprot.writeStructBegin('TDataPartition')
    if self.type is not None:
      oprot.writeFieldBegin('type', TType.I32, 1)
      oprot.writeI32(self.type)
      oprot.writeFieldEnd()
    if self.partition_exprs is not None:
      oprot.writeFieldBegin('partition_exprs', TType.LIST, 2)
      oprot.writeListBegin(TType.STRUCT, len(self.partition_exprs))
      for iter6 in self.partition_exprs:
        iter6.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.type is None:
      raise TProtocol.TProtocolException(message='Required field type is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
