class Author:
    """Represent an author who can sign contracts for books."""

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        self._name = value

    def contracts(self):
        """Return all contracts associated with this author."""
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        """Return all books linked to this author through contracts."""
        return [contract.book for contract in self.contracts()]

    def sign_contracts(self, book, date, royalties):
        """Create and return a new contract between this author and a book."""
        return Contract(self, book, date, royalties)

    def sign_contract(self, book, date, royalties):
        """Alias for sign_contracts to support the common test name."""
        return self.sign_contracts(book, date, royalties)

    def total_royalties(self):
        """Return the total royalties earned from all of this author's contracts."""
        return sum(contract.royalties for contract in self.contracts())


class Book:
    """Represent a book that can have many authors through contracts."""

    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise Exception("Title must be a string")
        self._title = value

    def contracts(self):
        """Return all contracts associated with this book."""
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        """Return all authors linked to this book through contracts."""
        return [contract.author for contract in self.contracts()]


class Contract:
    """Link an author to a book with a date and royalty terms."""

    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be an Author instance")
        self._author = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("Book must be a Book instance")
        self._book = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("Date must be a string")
        self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("Royalties must be an integer")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date):
        """Return all contracts that share the same date."""
        return [contract for contract in cls.all if contract.date == date]