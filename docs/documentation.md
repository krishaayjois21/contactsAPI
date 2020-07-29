

# Documentation for API

### List All Contacts stored in Database

Endpoint

`GET /contacts`

Response

- `200 OK` on success

```json
{
	"message": "success",
	"data": 
    [
        {
        	"name": "John Doe",
        	"number": "98201805430",
        	"email": "john.doe@email.com",
        	"contact-id": "4256344"
        },
        {
        	"name": "Jenna Doe",
        	"number": "98298805430",
        	"email": "jenna.doe@email.com",
        	"contact-id": "7865690"
        }
    ]
}
```

### Add A new contact to the Database

Endpoint

`POST /contacts`

Arguments

- `name` Name of the contact 
- `number` Phone Number of the contact
- `email` Email ID of the contact (optional)
- `contact-id` Uniques identifier for the contact

If a contact already exists with the mentioned identifier it will be overwritten

Response

- `201 Created` on success

```json
{
	"message": "created",
	"data": 
    {
        "name": "Jack Ryan",
        "number": "54353465364",
        "email": "jack.ryan@examplemail.com",
        "contact-id": "64564565464"
    }
}
```

### Get Details for a specific contact

Endpoint

`GET /contact/<identifier>`

Response

- `200 OK` on success
- `404 Not found` if contact does not exist

200 Code Response

```json
{
	"message": "success",
	"data": 
    {
        "name": "Jack Ryan",
        "number": "54353465364",
        "email": "jack.ryan@examplemail.com",
        "contact-id": "64564565464"
    }
}
```

404 Code response

```json
{
	"message": "not found",
	"data":{}

}
```

### Deleting a contact from the Database

Endpoint

`DELETE /contact/<identifier>`

Response

- `204 No content` on success
- `404 Not Found` when not found

204 Code Response

```json
{
	"message": "deleted",
	"data":{}

}
```

404 Code response

```json
{
	"message": "not found",
	"data": {}
}
```
