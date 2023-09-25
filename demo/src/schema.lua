local typedefs = require "kong.db.schema.typedefs"

return {
  name = "demo",
  fields = {
    {
      protocols = typedefs.protocols_http,
    },
    {
      config = {
        type = "record",
        fields = {
            {  user = { type = "string", required = true, default  = "admin" }, },
        },
      },
    },
  },
  entity_checks = {},
}
