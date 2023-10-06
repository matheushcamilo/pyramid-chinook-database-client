from slashdb.database.models import Customer, DBSession
from slashdb.views.default import (
    CustomerListView,
    FilteredCustomerListView,
    ArtistListView,
    FilteredArtistListView,
    InvoiceListView,
    FilteredInvoiceListView,
    TrackListView,
    FilteredTrackListView,
    PlaylistListView,
    FilteredPlaylistListView,
)
from tests.conftest import dummy_request


def __get_test_customer_data():
    american_customer = DBSession.query(Customer).filter(
        Customer.FirstName == 'Jack'
    ).filter(
        Customer.LastName == 'Smith'
    ).first()
    brazilian_customer = DBSession.query(Customer).filter(
        Customer.FirstName == 'Alexandre'
    ).filter(
        Customer.LastName == 'Rocha'
    ).first()

    return american_customer, brazilian_customer


def test_customer_list_view(dummy_request):
    # Check if the complete list of customers is returned

    view = CustomerListView(dummy_request)

    response = view()

    customers = response['items']

    american_customer, brazilian_customer = __get_test_customer_data()

    assert american_customer in customers and brazilian_customer in customers


def test_filtered_customer_list_view(dummy_request):
    # Check if the filters are working

    dummy_request.matchdict = {'filter_attr': 'Country', 'filter_value': 'USA'}
    view = FilteredCustomerListView(dummy_request)
    response = view()

    customers = response['items']

    american_customer, brazilian_customer = __get_test_customer_data()

    assert american_customer in customers and brazilian_customer not in customers


def test_artist_list(dummy_request):
    # Check if the complete list of artists is returned

    view = ArtistListView(dummy_request)

    response = view()

    artists = response['items']

    assert len(artists) == 275


def test_filtered_artist_list(dummy_request):
    # Check if the name filter is working

    dummy_request.matchdict = {'filter_attr': 'Name', 'filter_value': 'Aerosmith'}
    view = FilteredArtistListView(dummy_request)
    response = view()

    artists = response['items']

    assert len(artists) == 1


def test_invoice_list(dummy_request):
    # Check if the complete list of invoices is returned

    view = InvoiceListView(dummy_request)

    response = view()

    invoices = response['items']

    assert len(invoices) == 412


def test_track_list(dummy_request):
    # Check if the complete list of tracks is returned

    view = TrackListView(dummy_request)

    response = view()

    tracks = response['items']

    assert len(tracks) == 3503


def test_playlist_list(dummy_request):
    # Check if the complete list of playlists is returned

    view = PlaylistListView(dummy_request)

    response = view()

    playlists = response['items']

    assert len(playlists) == 18


def test_filtered_playlist_list(dummy_request):
    # Check if the name filter is working

    dummy_request.matchdict = {'filter_attr': 'Name', 'filter_value': 'Music'}
    view = FilteredPlaylistListView(dummy_request)
    response = view()

    playlists = response['items']

    assert len(playlists) == 2
