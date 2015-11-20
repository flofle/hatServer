# coding: utf-8
import pyjsonrpc
import random

class Room:
    def __init__(self,ownerid, id = 0 ):
        if id == 0:
            self.id = random.randint(0,100)
        else:
            self.id = id
        self.ownerid = ownerid
        return self.id

class Rooms:
    def __init__(self):
        self.RoomContainer = []
    def addRoom(self, ownerid):
        self.RoomContainer.append(Room(ownerid))


class HatServer:

    class RequestHandler(pyjsonrpc.HttpRequestHandler):

        roomContainer = Rooms

        @pyjsonrpc.rpcmethod
        def addRoom(self, ownid):
            self.on_append(ownid)
            return "OK"

        @pyjsonrpc.rpcmethod
        def register(self, ownid, roomid):
            self.on_register(ownid, roomid)
            return "OK"

        def on_register(self, cliid, room):
            return 0

        def on_append(self,ownid):
            self.roomContainer.addRoom(ownid)
            return 0


    def __init__(self, startport, starthost):
        print("Starting Server with port: "+str(startport)+". On host:"+starthost+".")
        http_server = pyjsonrpc.ThreadingHttpServer(
            server_address=(starthost,startport),
            RequestHandlerClass = self.RequestHandler
        )
        print("Starting http server")
        try:
            http_server.serve_forever()
        except KeyboardInterrupt:
            http_server.shutdown()
        print("Stoping server")



if __name__ == "__main__":
    PORT = 8005
    HOST = "0.0.0.0"
    try:
        import argparse

        arparser = argparse.ArgumentParser(description='Game server for hats')
        arparser.add_argument('-p', '--p', type=int, dest='PORT',
                              help='the port to run the server on; defaults to 8003')
        arparser.add_argument('-s', '--s', type=int, dest='HOST',
                              help='the host to run the server on; defaults to anyhost')

        args= arparser.parse_args()

        if args.PORT:
            PORT = args.PORT
        if args.HOST:
            HOST = args.HOST
    except:
        # Could not successfully import argparse or something
        pass

    hServer = HatServer(PORT,HOST)
