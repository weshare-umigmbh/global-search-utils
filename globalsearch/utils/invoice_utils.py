from mergedeep import merge


def get_invoice_search_result(client, invoice_id):
    body_get_invoice = {
        "query": {
            "match_phrase": {
                "_id": invoice_id
            }
        }
    }
    search_invoice_result = client.search(index="invoices*", body=body_get_invoice, seq_no_primary_term=True)
    return search_invoice_result


def upsert_invoice(client, stored_invoice_doc, entity):
    if stored_invoice_doc is None:
        response = client.index(index="alias-invoices", id=entity.get("id"),
                                document=entity)
    else:
        response = client.index(index="alias-invoices", id=entity.get("id"),
                                document=entity, if_seq_no=stored_invoice_doc.get('_seq_no'),
                                if_primary_term=stored_invoice_doc.get('_primary_term'))
    return response


def merge_invoice_to_save(invoice, stored_invoice_doc):
    if stored_invoice_doc is None:
        return invoice

    old_invoice = stored_invoice_doc.get("_source", {})
    new_invoice = merge(old_invoice, invoice)

    return new_invoice
