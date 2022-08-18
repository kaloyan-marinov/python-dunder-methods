class Client:
    """
    Assume that
    it is very expensive to instantiate this class
    (because, for example, doing so requires
    reading from a database
    or reading from a file).

    This is similar to how some big frameworks work.
    """

    _client_id_2_client = {}
    _db_file = 'db.sqlite3'

    def __new__(cls, client_id):
        client = cls._client_id_2_client.get(client_id)

        if client is not None:
            print(f'returning existing client (with ID {client_id}) from cache')
            return client
        
        client = super().__new__(cls)
        cls._client_id_2_client[client_id] = client
        client._init_from_file(client_id, cls._db_file)

        return client
    
    def _init_from_file(self, client_id, file):
        """Look up the client and read client's info."""
        print(f'reading info about client (with ID {client_id}) from {file}')
        # name = ...
        # email = ...
        # self.id = client_id
        # self.name = name
        # self.email = email


def cached_clients_example():
    print('CLIENT CACHE EXAMPLE')

    print()
    x = Client(0)
    y = Client(0)
    print('x is y:', x is y)

    print()
    z = Client(1)


if __name__ == '__main__':
    cached_clients_example()
