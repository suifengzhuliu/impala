#
# Autogenerated by Thrift Compiler (0.9.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import CatalogObjects.ttypes
import Types.ttypes
import Exprs.ttypes


from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class TSlotDescriptor:
  """
  Attributes:
   - id
   - parent
   - itemTupleId
   - slotType
   - materializedPath
   - byteOffset
   - nullIndicatorByte
   - nullIndicatorBit
   - slotIdx
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'id', None, None, ), # 1
    (2, TType.I32, 'parent', None, None, ), # 2
    (3, TType.I32, 'itemTupleId', None, None, ), # 3
    (4, TType.STRUCT, 'slotType', (Types.ttypes.TColumnType, Types.ttypes.TColumnType.thrift_spec), None, ), # 4
    (5, TType.LIST, 'materializedPath', (TType.I32,None), None, ), # 5
    (6, TType.I32, 'byteOffset', None, None, ), # 6
    (7, TType.I32, 'nullIndicatorByte', None, None, ), # 7
    (8, TType.I32, 'nullIndicatorBit', None, None, ), # 8
    (9, TType.I32, 'slotIdx', None, None, ), # 9
  )

  def __init__(self, id=None, parent=None, itemTupleId=None, slotType=None, materializedPath=None, byteOffset=None, nullIndicatorByte=None, nullIndicatorBit=None, slotIdx=None,):
    self.id = id
    self.parent = parent
    self.itemTupleId = itemTupleId
    self.slotType = slotType
    self.materializedPath = materializedPath
    self.byteOffset = byteOffset
    self.nullIndicatorByte = nullIndicatorByte
    self.nullIndicatorBit = nullIndicatorBit
    self.slotIdx = slotIdx

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
          self.id = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.parent = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.itemTupleId = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRUCT:
          self.slotType = Types.ttypes.TColumnType()
          self.slotType.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.LIST:
          self.materializedPath = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = iprot.readI32();
            self.materializedPath.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I32:
          self.byteOffset = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.I32:
          self.nullIndicatorByte = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.I32:
          self.nullIndicatorBit = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.I32:
          self.slotIdx = iprot.readI32();
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
    oprot.writeStructBegin('TSlotDescriptor')
    if self.id is not None:
      oprot.writeFieldBegin('id', TType.I32, 1)
      oprot.writeI32(self.id)
      oprot.writeFieldEnd()
    if self.parent is not None:
      oprot.writeFieldBegin('parent', TType.I32, 2)
      oprot.writeI32(self.parent)
      oprot.writeFieldEnd()
    if self.itemTupleId is not None:
      oprot.writeFieldBegin('itemTupleId', TType.I32, 3)
      oprot.writeI32(self.itemTupleId)
      oprot.writeFieldEnd()
    if self.slotType is not None:
      oprot.writeFieldBegin('slotType', TType.STRUCT, 4)
      self.slotType.write(oprot)
      oprot.writeFieldEnd()
    if self.materializedPath is not None:
      oprot.writeFieldBegin('materializedPath', TType.LIST, 5)
      oprot.writeListBegin(TType.I32, len(self.materializedPath))
      for iter6 in self.materializedPath:
        oprot.writeI32(iter6)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.byteOffset is not None:
      oprot.writeFieldBegin('byteOffset', TType.I32, 6)
      oprot.writeI32(self.byteOffset)
      oprot.writeFieldEnd()
    if self.nullIndicatorByte is not None:
      oprot.writeFieldBegin('nullIndicatorByte', TType.I32, 7)
      oprot.writeI32(self.nullIndicatorByte)
      oprot.writeFieldEnd()
    if self.nullIndicatorBit is not None:
      oprot.writeFieldBegin('nullIndicatorBit', TType.I32, 8)
      oprot.writeI32(self.nullIndicatorBit)
      oprot.writeFieldEnd()
    if self.slotIdx is not None:
      oprot.writeFieldBegin('slotIdx', TType.I32, 9)
      oprot.writeI32(self.slotIdx)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.id is None:
      raise TProtocol.TProtocolException(message='Required field id is unset!')
    if self.parent is None:
      raise TProtocol.TProtocolException(message='Required field parent is unset!')
    if self.slotType is None:
      raise TProtocol.TProtocolException(message='Required field slotType is unset!')
    if self.materializedPath is None:
      raise TProtocol.TProtocolException(message='Required field materializedPath is unset!')
    if self.byteOffset is None:
      raise TProtocol.TProtocolException(message='Required field byteOffset is unset!')
    if self.nullIndicatorByte is None:
      raise TProtocol.TProtocolException(message='Required field nullIndicatorByte is unset!')
    if self.nullIndicatorBit is None:
      raise TProtocol.TProtocolException(message='Required field nullIndicatorBit is unset!')
    if self.slotIdx is None:
      raise TProtocol.TProtocolException(message='Required field slotIdx is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TColumnDescriptor:
  """
  Attributes:
   - name
   - type
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'name', None, None, ), # 1
    (2, TType.STRUCT, 'type', (Types.ttypes.TColumnType, Types.ttypes.TColumnType.thrift_spec), None, ), # 2
  )

  def __init__(self, name=None, type=None,):
    self.name = name
    self.type = type

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
          self.name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.type = Types.ttypes.TColumnType()
          self.type.read(iprot)
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
    oprot.writeStructBegin('TColumnDescriptor')
    if self.name is not None:
      oprot.writeFieldBegin('name', TType.STRING, 1)
      oprot.writeString(self.name)
      oprot.writeFieldEnd()
    if self.type is not None:
      oprot.writeFieldBegin('type', TType.STRUCT, 2)
      self.type.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.name is None:
      raise TProtocol.TProtocolException(message='Required field name is unset!')
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

class TTableDescriptor:
  """
  Attributes:
   - id
   - tableType
   - columnDescriptors
   - numClusteringCols
   - hdfsTable
   - hbaseTable
   - dataSourceTable
   - kuduTable
   - tableName
   - dbName
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'id', None, None, ), # 1
    (2, TType.I32, 'tableType', None, None, ), # 2
    (3, TType.LIST, 'columnDescriptors', (TType.STRUCT,(TColumnDescriptor, TColumnDescriptor.thrift_spec)), None, ), # 3
    (4, TType.I32, 'numClusteringCols', None, None, ), # 4
    (5, TType.STRUCT, 'hdfsTable', (CatalogObjects.ttypes.THdfsTable, CatalogObjects.ttypes.THdfsTable.thrift_spec), None, ), # 5
    (6, TType.STRUCT, 'hbaseTable', (CatalogObjects.ttypes.THBaseTable, CatalogObjects.ttypes.THBaseTable.thrift_spec), None, ), # 6
    (7, TType.STRING, 'tableName', None, None, ), # 7
    (8, TType.STRING, 'dbName', None, None, ), # 8
    (9, TType.STRUCT, 'dataSourceTable', (CatalogObjects.ttypes.TDataSourceTable, CatalogObjects.ttypes.TDataSourceTable.thrift_spec), None, ), # 9
    (10, TType.STRUCT, 'kuduTable', (CatalogObjects.ttypes.TKuduTable, CatalogObjects.ttypes.TKuduTable.thrift_spec), None, ), # 10
  )

  def __init__(self, id=None, tableType=None, columnDescriptors=None, numClusteringCols=None, hdfsTable=None, hbaseTable=None, dataSourceTable=None, kuduTable=None, tableName=None, dbName=None,):
    self.id = id
    self.tableType = tableType
    self.columnDescriptors = columnDescriptors
    self.numClusteringCols = numClusteringCols
    self.hdfsTable = hdfsTable
    self.hbaseTable = hbaseTable
    self.dataSourceTable = dataSourceTable
    self.kuduTable = kuduTable
    self.tableName = tableName
    self.dbName = dbName

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
          self.id = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.tableType = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.columnDescriptors = []
          (_etype10, _size7) = iprot.readListBegin()
          for _i11 in xrange(_size7):
            _elem12 = TColumnDescriptor()
            _elem12.read(iprot)
            self.columnDescriptors.append(_elem12)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.numClusteringCols = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRUCT:
          self.hdfsTable = CatalogObjects.ttypes.THdfsTable()
          self.hdfsTable.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRUCT:
          self.hbaseTable = CatalogObjects.ttypes.THBaseTable()
          self.hbaseTable.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.STRUCT:
          self.dataSourceTable = CatalogObjects.ttypes.TDataSourceTable()
          self.dataSourceTable.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.STRUCT:
          self.kuduTable = CatalogObjects.ttypes.TKuduTable()
          self.kuduTable.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.STRING:
          self.tableName = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.STRING:
          self.dbName = iprot.readString();
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
    oprot.writeStructBegin('TTableDescriptor')
    if self.id is not None:
      oprot.writeFieldBegin('id', TType.I32, 1)
      oprot.writeI32(self.id)
      oprot.writeFieldEnd()
    if self.tableType is not None:
      oprot.writeFieldBegin('tableType', TType.I32, 2)
      oprot.writeI32(self.tableType)
      oprot.writeFieldEnd()
    if self.columnDescriptors is not None:
      oprot.writeFieldBegin('columnDescriptors', TType.LIST, 3)
      oprot.writeListBegin(TType.STRUCT, len(self.columnDescriptors))
      for iter13 in self.columnDescriptors:
        iter13.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.numClusteringCols is not None:
      oprot.writeFieldBegin('numClusteringCols', TType.I32, 4)
      oprot.writeI32(self.numClusteringCols)
      oprot.writeFieldEnd()
    if self.hdfsTable is not None:
      oprot.writeFieldBegin('hdfsTable', TType.STRUCT, 5)
      self.hdfsTable.write(oprot)
      oprot.writeFieldEnd()
    if self.hbaseTable is not None:
      oprot.writeFieldBegin('hbaseTable', TType.STRUCT, 6)
      self.hbaseTable.write(oprot)
      oprot.writeFieldEnd()
    if self.tableName is not None:
      oprot.writeFieldBegin('tableName', TType.STRING, 7)
      oprot.writeString(self.tableName)
      oprot.writeFieldEnd()
    if self.dbName is not None:
      oprot.writeFieldBegin('dbName', TType.STRING, 8)
      oprot.writeString(self.dbName)
      oprot.writeFieldEnd()
    if self.dataSourceTable is not None:
      oprot.writeFieldBegin('dataSourceTable', TType.STRUCT, 9)
      self.dataSourceTable.write(oprot)
      oprot.writeFieldEnd()
    if self.kuduTable is not None:
      oprot.writeFieldBegin('kuduTable', TType.STRUCT, 10)
      self.kuduTable.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.id is None:
      raise TProtocol.TProtocolException(message='Required field id is unset!')
    if self.tableType is None:
      raise TProtocol.TProtocolException(message='Required field tableType is unset!')
    if self.columnDescriptors is None:
      raise TProtocol.TProtocolException(message='Required field columnDescriptors is unset!')
    if self.numClusteringCols is None:
      raise TProtocol.TProtocolException(message='Required field numClusteringCols is unset!')
    if self.tableName is None:
      raise TProtocol.TProtocolException(message='Required field tableName is unset!')
    if self.dbName is None:
      raise TProtocol.TProtocolException(message='Required field dbName is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TTupleDescriptor:
  """
  Attributes:
   - id
   - byteSize
   - numNullBytes
   - tableId
   - tuplePath
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'id', None, None, ), # 1
    (2, TType.I32, 'byteSize', None, None, ), # 2
    (3, TType.I32, 'numNullBytes', None, None, ), # 3
    (4, TType.I32, 'tableId', None, None, ), # 4
    (5, TType.LIST, 'tuplePath', (TType.I32,None), None, ), # 5
  )

  def __init__(self, id=None, byteSize=None, numNullBytes=None, tableId=None, tuplePath=None,):
    self.id = id
    self.byteSize = byteSize
    self.numNullBytes = numNullBytes
    self.tableId = tableId
    self.tuplePath = tuplePath

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
          self.id = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.byteSize = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.numNullBytes = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.tableId = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.LIST:
          self.tuplePath = []
          (_etype17, _size14) = iprot.readListBegin()
          for _i18 in xrange(_size14):
            _elem19 = iprot.readI32();
            self.tuplePath.append(_elem19)
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
    oprot.writeStructBegin('TTupleDescriptor')
    if self.id is not None:
      oprot.writeFieldBegin('id', TType.I32, 1)
      oprot.writeI32(self.id)
      oprot.writeFieldEnd()
    if self.byteSize is not None:
      oprot.writeFieldBegin('byteSize', TType.I32, 2)
      oprot.writeI32(self.byteSize)
      oprot.writeFieldEnd()
    if self.numNullBytes is not None:
      oprot.writeFieldBegin('numNullBytes', TType.I32, 3)
      oprot.writeI32(self.numNullBytes)
      oprot.writeFieldEnd()
    if self.tableId is not None:
      oprot.writeFieldBegin('tableId', TType.I32, 4)
      oprot.writeI32(self.tableId)
      oprot.writeFieldEnd()
    if self.tuplePath is not None:
      oprot.writeFieldBegin('tuplePath', TType.LIST, 5)
      oprot.writeListBegin(TType.I32, len(self.tuplePath))
      for iter20 in self.tuplePath:
        oprot.writeI32(iter20)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.id is None:
      raise TProtocol.TProtocolException(message='Required field id is unset!')
    if self.byteSize is None:
      raise TProtocol.TProtocolException(message='Required field byteSize is unset!')
    if self.numNullBytes is None:
      raise TProtocol.TProtocolException(message='Required field numNullBytes is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TDescriptorTable:
  """
  Attributes:
   - slotDescriptors
   - tupleDescriptors
   - tableDescriptors
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'slotDescriptors', (TType.STRUCT,(TSlotDescriptor, TSlotDescriptor.thrift_spec)), None, ), # 1
    (2, TType.LIST, 'tupleDescriptors', (TType.STRUCT,(TTupleDescriptor, TTupleDescriptor.thrift_spec)), None, ), # 2
    (3, TType.LIST, 'tableDescriptors', (TType.STRUCT,(TTableDescriptor, TTableDescriptor.thrift_spec)), None, ), # 3
  )

  def __init__(self, slotDescriptors=None, tupleDescriptors=None, tableDescriptors=None,):
    self.slotDescriptors = slotDescriptors
    self.tupleDescriptors = tupleDescriptors
    self.tableDescriptors = tableDescriptors

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
        if ftype == TType.LIST:
          self.slotDescriptors = []
          (_etype24, _size21) = iprot.readListBegin()
          for _i25 in xrange(_size21):
            _elem26 = TSlotDescriptor()
            _elem26.read(iprot)
            self.slotDescriptors.append(_elem26)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.tupleDescriptors = []
          (_etype30, _size27) = iprot.readListBegin()
          for _i31 in xrange(_size27):
            _elem32 = TTupleDescriptor()
            _elem32.read(iprot)
            self.tupleDescriptors.append(_elem32)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.tableDescriptors = []
          (_etype36, _size33) = iprot.readListBegin()
          for _i37 in xrange(_size33):
            _elem38 = TTableDescriptor()
            _elem38.read(iprot)
            self.tableDescriptors.append(_elem38)
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
    oprot.writeStructBegin('TDescriptorTable')
    if self.slotDescriptors is not None:
      oprot.writeFieldBegin('slotDescriptors', TType.LIST, 1)
      oprot.writeListBegin(TType.STRUCT, len(self.slotDescriptors))
      for iter39 in self.slotDescriptors:
        iter39.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.tupleDescriptors is not None:
      oprot.writeFieldBegin('tupleDescriptors', TType.LIST, 2)
      oprot.writeListBegin(TType.STRUCT, len(self.tupleDescriptors))
      for iter40 in self.tupleDescriptors:
        iter40.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.tableDescriptors is not None:
      oprot.writeFieldBegin('tableDescriptors', TType.LIST, 3)
      oprot.writeListBegin(TType.STRUCT, len(self.tableDescriptors))
      for iter41 in self.tableDescriptors:
        iter41.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.tupleDescriptors is None:
      raise TProtocol.TProtocolException(message='Required field tupleDescriptors is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
