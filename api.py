from firebaseInit import db
from flask import Flask , render_template
from flask_restful import Api , Resource , reqparse

app = Flask(__name__)
api = Api(app)

@app.route('/')
def documentation():
    '''Give API documentation to user'''
    return render_template('docs.html')

class Contacts(Resource):
    def get(self):
        contacts_collection = db.collection(u'contacts')
        contacts = contacts_collection.stream()
        contact_data = []
        for contact in contacts:
            contact_data.append(contact.to_dict())
        return {
            'message': 'success',
            'data': contact_data
        } , 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name' , required=True)
        parser.add_argument('number' ,required=True)
        parser.add_argument('email' , required=False)
        parser.add_argument('contact-id', required=True)
        args = parser.parse_args()

        contact_data = {
            u'name': args['name'],
            u'number': args['number'],
            u'contact-id': args['contact-id']
        }

        if args['email']:
            contact_data['email'] = args['email']

        contact_collection =  db.collection(u'contacts').document(u'{id}'.format(id=args['contact-id']))
        contact_collection.set(contact_data)

        return {
            'message':'created',
            'data': contact_data,
               } , 201


class Contact(Resource):

    def get(self , contact_id):
        contact_doc =  db.collection(u'contacts').document(u'{id}'.format(id=contact_id))
        contact = contact_doc.get()
        if contact.exists:
            return {
            'message': 'success',
            'data': contact.to_dict()
            } , 200
        else:
            return {
                'message': 'not found',
                'data': {}
            } , 404

    def delete(self , contact_id):
        contact_doc = db.collection(u'contacts').document(u'{id}'.format(id=contact_id))
        contact_data = contact_doc.get()

        if contact_data.exists:
            contact_doc.delete()
            return {
                'message': 'deleted',
                'data': {},
            } , 204
        else:
            return {
                'message': 'not found',
                'data': {},
            } , 404


api.add_resource(Contacts , '/contacts')
api.add_resource(Contact , '/contact/<string:contact_id>')
