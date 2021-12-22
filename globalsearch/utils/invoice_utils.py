from globalsearch.utils.elastic_uitls import assemble_update_body


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


def create_or_update_invoice(client, stored_invoice_doc, transaction):
    if stored_invoice_doc is None:
        response = client.index(index="alias-invoices", pipeline="pipeline-invoices", id=transaction.get("id"),
                                document=transaction)
    else:
        response = client.update(id=stored_invoice_doc.get('_id'), index=stored_invoice_doc.get('_index'),
                                 body=assemble_update_body(transaction), if_seq_no=stored_invoice_doc.get('_seq_no'),
                                 if_primary_term=stored_invoice_doc.get('_primary_term'))
    return response
