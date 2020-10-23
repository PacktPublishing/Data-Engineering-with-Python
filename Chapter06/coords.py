import urllib
import urllib2
import json
import java.io
from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import StreamCallback
from org.python.core.util import StringUtil

class ModJSON(StreamCallback):
  def __init__(self):
        pass
  def process(self, inputStream, outputStream):
    try:
        text = IOUtils.toString(inputStream, StandardCharsets.UTF_8)
        reply=json.loads(text)
        
        reply['coords']=str(reply['lat'])+","+str(reply['lng'])
        d=reply['created_at'].split("T")
        reply['opendate']=d[0]
        outputStream.write(bytearray(json.dumps(reply, indent=4).encode('utf-8')))
    except:
        global errorOccurred
        errorOccurred=True
        
        outputStream.write(bytearray(json.dumps(reply, indent=4).encode('utf-8')))
        
errorOccurred=False
flowFile = session.get()
if (flowFile != None):
  flowFile = session.write(flowFile, ModJSON())
  #flowFile = session.putAttribute(flowFile)
  if(errorOccurred):
    session.transfer(flowFile, REL_FAILURE)
  
  else:
    session.transfer(flowFile, REL_SUCCESS)
  
session.commit()

