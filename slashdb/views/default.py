from pyramid.view import view_config
from ..database.models import (
    Album, Artist, Invoice, Track, Customer, DBSession, Playlist
)


class BaseView:
    def __init__(self, request):
        self.request = request
        self.db_session = DBSession()

    def __del__(self):
        self.db_session.close()


class UnfilteredListView(BaseView):
    def __init__(self, request, model):
        super().__init__(request)
        self.model = model

    def __call__(self):
        items = self.db_session.query(self.model).all()
        return {'items': items}


class FilteredListView(BaseView):
    def __init__(self, request, model):
        super().__init__(request)
        self.model = model
        self.filter_attr = request.matchdict.get('filter_attr', None)
        self.filter_value = request.matchdict.get('filter_value', None)

    def __call__(self):
        query = self.db_session.query(self.model)

        if self.filter_attr and self.filter_value:
            filter_column = getattr(self.model, self.filter_attr.title(), None)
            if filter_column:
                query = query.filter(filter_column == self.filter_value)

        items = query.all()
        return {'items': items}


@view_config(route_name='album_list', renderer='albums.mako')
class AlbumListView(UnfilteredListView):
    def __init__(self, request):
        super().__init__(request, Album)


@view_config(route_name='filtered_album_list', renderer='albums.mako')
class FilteredAlbumListView(FilteredListView):
    def __init__(self, request):
        super().__init__(request, Album)


@view_config(route_name='artist_list', renderer='artists.mako')
class ArtistListView(UnfilteredListView):
    def __init__(self, request):
        super().__init__(request, Artist)


@view_config(route_name='filtered_artist_list', renderer='artists.mako')
class FilteredArtistListView(FilteredListView):
    def __init__(self, request):
        super().__init__(request, Artist)


@view_config(route_name='invoice_list', renderer='invoices.mako')
class InvoiceListView(UnfilteredListView):
    def __init__(self, request):
        super().__init__(request, Invoice)


@view_config(route_name='filtered_invoice_list', renderer='invoices.mako')
class FilteredInvoiceListView(FilteredListView):
    def __init__(self, request):
        super().__init__(request, Invoice)


@view_config(route_name='track_list', renderer='tracks.mako')
class TrackListView(UnfilteredListView):
    def __init__(self, request):
        super().__init__(request, Track)


@view_config(route_name='filtered_track_list', renderer='tracks.mako')
class FilteredTrackListView(FilteredListView):
    def __init__(self, request):
        super().__init__(request, Track)


@view_config(route_name='playlist_list', renderer='playlists.mako')
class PlaylistListView(UnfilteredListView):
    def __init__(self, request):
        super().__init__(request, Playlist)


@view_config(route_name='filtered_playlist_list', renderer='playlists.mako')
class FilteredPlaylistListView(FilteredListView):
    def __init__(self, request):
        super().__init__(request, Playlist)


@view_config(route_name='customer_list', renderer='customers.mako')
class CustomerListView(UnfilteredListView):
    def __init__(self, request):
        super().__init__(request, Customer)


@view_config(route_name='filtered_customer_list', renderer='customers.mako')
class FilteredCustomerListView(FilteredListView):
    def __init__(self, request):
        super().__init__(request, Customer)
