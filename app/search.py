from flask import current_app


def add_to_index(index, model):
    """ Adds the given fields from specified model
        defined by the __searchable__ property
        to the index of full text search

        args:
            index: the index for the full text search service
            model: a SQLAlchemy model that contains the __searchable__ array
    """
    # Check if the elasticsearch eninge is connected
    if not current_app.elasticsearch:
        return
    payload = {}

    # Iterate over __searchale__ array and store in payload dictionary
    for field in model.__searchable__:
        payload[field] = getattr(model, field)

    # After payload is build call the index method on elasticsearch
    current_app.elasticsearch.index(index=index, doc_type=index, id=model.id,
                                    body=payload)

def remove_from_index(index, model):
    if not current_app.elasticsearch:
        return
    current_app.elasticsearch.delete(index=index, doc_type=index,id=model.id)


def query_index(index, query, page, per_page):
    """
        Query's the full text search engine.

        args:
            index: The index or database file name of the search engine
            query: The text used to search the database
            page: the current pagin
            per page: the amount of results to return per page

        returns:
            ids: The unique ids that match with the relational db
            search: the actual search results
    """
    if not current_app.elasticsearch:
        return [], 0
    search = current_app.elasticsearch.search(
        index=index,
        body={'query': {'multi_match': {'query': query, 'fields': ['*']}},
              'from': (page - 1) * per_page, 'size': per_page})
    ids = [int(hit['_id']) for hit in search['hits']['hits']]
    return ids, search['hits']['total']
