from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker, relationship,
)

from zope.sqlalchemy import register

DBSession = scoped_session(sessionmaker())
register(DBSession)
Base = declarative_base()


class Album(Base):
    __tablename__ = 'Album'

    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String(160), nullable=False)
    ArtistId = Column(Integer, ForeignKey('Artist.ArtistId'))

    Artist = relationship('Artist', back_populates='Albums')

    def __str__(self):
        return f"{self.Title}"

    def __repr__(self):
        return f"<Album: {self.Title}>"

    def __eq__(self, other):
        return self.AlbumId == other.AlbumId

    def __hash__(self):
        return hash(self.AlbumId)


class Artist(Base):
    __tablename__ = 'Artist'

    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String(120))

    Albums = relationship('Album', back_populates='Artist')

    def __str__(self):
        return f"{self.Name}"

    def __repr__(self):
        return f"<Artist: {self.Name}>"

    def __eq__(self, other):
        return self.ArtistId == other.ArtistId

    def __hash__(self):
        return hash(self.ArtistId)


class Customer(Base):
    __tablename__ = 'Customer'

    CustomerId = Column(Integer, primary_key=True)
    FirstName = Column(String(50), nullable=False)
    LastName = Column(String(50), nullable=False)
    Company = Column(String(255), nullable=False)
    Address = Column(String(255), nullable=False)
    City = Column(String(50), nullable=False)
    State = Column(String(50), nullable=False)
    Country = Column(String(50), nullable=False)
    PostalCode = Column(String(50), nullable=False)
    Phone = Column(String(50), nullable=False)
    Fax = Column(String(50), nullable=False)
    Email = Column(String(255), nullable=False)

    SupportRep = relationship('Employee', back_populates='Customers')
    SupportRepId = Column(Integer, ForeignKey('Employee.EmployeeId'))

    def __str__(self):
        return f"{self.FirstName} - {self.LastName} - {self.Company}"

    def __repr__(self):
        return f"<Customer: {self.FirstName} - {self.LastName} - {self.Company}>"

    def __eq__(self, other):
        return self.CustomerId == other.CustomerId

    def __hash__(self):
        return hash(self.CustomerId)


class Employee(Base):
    __tablename__ = 'Employee'

    EmployeeId = Column(Integer, primary_key=True)
    LastName = Column(String(20), nullable=False)
    FirstName = Column(String(20), nullable=False)
    Title = Column(String(30), nullable=False)
    ReportsTo = ForeignKey('Employee.id')
    BirthDate = Column(String(10))
    HireDate = Column(String(10))
    Address = Column(String(70))
    City = Column(String(40))
    State = Column(String(40))
    Country = Column(String(40))
    PostalCode = Column(String(10))
    Phone = Column(String(24))
    Fax = Column(String(24))
    Email = Column(String(60))

    Customers = relationship('Customer', back_populates='SupportRep')

    def __str__(self):
        return f"{self.FirstName} - {self.LastName} - {self.Title}"

    def __repr__(self):
        return f"<Employee: {self.FirstName} - {self.LastName} - {self.Title}>"

    def __eq__(self, other):
        return self.EmployeeId == other.EmployeeId

    def __hash__(self):
        return hash(self.EmployeeId)


class Genre(Base):
    __tablename__ = 'Genre'

    GenreId = Column(Integer, primary_key=True)
    Name = Column(String(120))

    def __str__(self):
        return f"{self.Name}"

    def __repr__(self):
        return f"<Genre: {self.Name}>"

    def __eq__(self, other):
        return self.GenreId == other.GenreId

    def __hash__(self):
        return hash(self.GenreId)


class Invoice(Base):
    __tablename__ = 'Invoice'

    InvoiceId = Column(Integer, primary_key=True)
    CustomerId = Column(Integer, ForeignKey('Customer.CustomerId'))
    InvoiceDate = Column(String(10))
    BillingAddress = Column(String(70))
    BillingCity = Column(String(40))
    BillingState = Column(String(40))
    BillingCountry = Column(String(40))
    BillingPostalCode = Column(String(10))
    Total = Column(Integer)

    invoice_lines = relationship('InvoiceLine', back_populates='invoice')

    def __str__(self):
        return f"{self.InvoiceId} - {self.CustomerId} - {self.Total}"

    def __repr__(self):
        return f"<Invoice: {self.InvoiceId} - {self.CustomerId} - {self.Total}>"

    def __eq__(self, other):
        return self.InvoiceId == other.InvoiceId

    def __hash__(self):
        return hash(self.InvoiceId)


class InvoiceLine(Base):
    __tablename__ = 'InvoiceLine'

    InvoiceLineId = Column(Integer, primary_key=True)

    InvoiceId = Column(Integer, ForeignKey('Invoice.InvoiceId'))
    TrackId = Column(Integer, ForeignKey('Track.TrackId'))

    UnitPrice = Column(Integer)
    Quantity = Column(Integer)

    invoice = relationship('Invoice', back_populates='invoice_lines')
    track = relationship('Track', back_populates='invoice_lines')

    def __str__(self):
        return f"{self.InvoiceLineId} - {self.InvoiceId} - {self.TrackId}"

    def __repr__(self):
        return f"<InvoiceLine: {self.InvoiceLineId} - {self.InvoiceId} - {self.TrackId}>"

    def __eq__(self, other):
        return self.InvoiceLineId == other.InvoiceLineId

    def __hash__(self):
        return hash(self.InvoiceLineId)


class MediaType(Base):
    __tablename__ = 'MediaType'

    MediaTypeId = Column(Integer, primary_key=True)
    Name = Column(String(120))

    def __str__(self):
        return f"{self.Name}"

    def __repr__(self):
        return f"<MediaType: {self.Name}>"

    def __eq__(self, other):
        return self.MediaTypeId == other.MediaTypeId

    def __hash__(self):
        return hash(self.MediaTypeId)


playlist_track_association = Table(
    'PlaylistTrack',
    Base.metadata,
    Column('PlaylistId', Integer, ForeignKey('Playlist.PlaylistId')),
    Column('TrackId', Integer, ForeignKey('Track.TrackId'))
)


class Playlist(Base):
    __tablename__ = 'Playlist'

    PlaylistId = Column(Integer, primary_key=True)
    Name = Column(String(120))

    def __str__(self):
        return f"{self.Name}"

    def __repr__(self):
        return f"<Playlist: {self.Name}>"

    def __eq__(self, other):
        return self.PlaylistId == other.PlaylistId

    def __hash__(self):
        return hash(self.PlaylistId)


class Track(Base):
    __tablename__ = 'Track'

    TrackId = Column(Integer, primary_key=True)
    Name = Column(String(200))

    AlbumId = Column(Integer, ForeignKey('AlbumId'))
    MediaTypeId = Column(Integer, ForeignKey('MediaTypeId'))
    GenreId = Column(Integer, ForeignKey('GenreId'))

    Composer = Column(String(220))
    Milliseconds = Column(Integer)
    Bytes = Column(Integer)
    UnitPrice = Column(Integer)

    invoice_lines = relationship('InvoiceLine', back_populates='track')

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<Track: {self.name}>"

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
