# tarsier-input-mongodb

mongodb input plugin for tarsier.


## install

```bash
pip install tarsier-input-mongodb
```

## configuration

```yaml
in:
  type: mongodb
  url: mongodb://localhost:27017/test # mongodb uri. required
  collection: test # collection name. required
  conditions: # find conditions. it converts to dict. optional
    _id: 507f1f77bcf86cd799439011
```