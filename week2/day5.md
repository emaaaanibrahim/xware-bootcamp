
# ex:1

### How connect Mongo Compass to MongoDB
```sql
mongosh
```

### Design Messaging and Notification System in MongoDB
```sql
use message_notfication

db.messages.insert ({sender:{id:1,name:'sara'},reciever:{id:1,name:'eman'},message:{id:1,name:'ayat'}})

db.messages.find()
```
#### result

```
[
  {
    _id: ObjectId("62e12e0cc8c5959a5856f8c8"),
    sender: { id: 1, name: 'sara' },
    reciever: { id: 1, name: 'eman' },
    message: { id: 1, name: 'ayat' }
  }
]
```

```sql
db.notification.insert ({sender:{id:1,name:'sara'},reciever:{id:1,name:'eman'},type:{id:1,name:'short_message'},content:{id:1,name:'thankful'},is_read:{id:1,name:'ok'},created_at:{id:1,name:'may'}})
```

#### result 
```
db.notification.find ([
  {
    _id: ObjectId("62e13a0fc8c5959a5856f8c9"),
    sender: { id: 1, name: 'sara' },
    reciever: { id: 1, name: 'eman' },
    type: { id: 1, name: 'short_message' },
    content: { id: 1, name: 'thankful' },
    is_read: { id: 1, name: 'ok' },
    created_at: { id: 1, name: 'may' }
  }
]
)
```
_________________________________________________________________________________________________________________________________________________________

# ex: 2

### Retrieve Specific Professor (Choose Anyone) Notifications

```sql
db.notification.find({sender:{id:1}})
``` 
 
 
### Retrieve Specific Student (Choose Anyone) Messages With Specific Professor (Choose Anyone)

```sql
db.messages.find({sender: {id: 1},reciver:{id:1}})
```

### Change Some Notification To Be is_read is True
 
```sql
db.notification.updateOne({ is_read: {name:'ok'} , $set: { is_read : {name: null }} })
```

#### ALL THE EX:2 HAS NO RESULTS


