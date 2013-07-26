class AppServerError( Exception ):

    def __init__( self, value ):
        '''
        Constructor
        '''
        self.value = value
    
    def __str__( self ):
        return repr( self.value )
        