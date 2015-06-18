from boto.ec2.ec2object import TaggedEC2Object


class ExportTask(TaggedEC2Object):
    """
    Represents an EC2 ImportTask
    """

    def __init__(self, connection=None):
        TaggedEC2Object.__init__(self, connection)
        self.request_id = None
        self.description = None
        self.exportTaskId = None
        self.containerFormat = None
        self.diskImageFormat = None
        self.s3Bucket = None
        self.s3Key = None
        self.instanceId = None
        self.targetEnvironment = None
        self.state = None
        self.statusMessage = None
        
    def endElement(self, name, value, connection):
        if name == 'description':
            self.description = value
        elif name == 'exportTaskId':
            self.exportTaskId = value
        elif name == 'containerFormat':
            self.containerFormat = value
        elif name == 'diskImageFormat':
            self.diskImageFormat = value
        elif name == 's3Bucket':
            self.s3Bucket = value
        elif name == 's3Key':
            self.s3Key = value
        elif name == 'instanceId':
            self.instanceId = value
        elif name == 'targetEnvironment':
            self.targetEnvironment = value
        elif name == 'state':
            self.state = value
        elif name == 'statusMessage':
            self.statusMessage = value
