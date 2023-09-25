package = "demo"
version = "1.0.0-0" 

supported_platforms = {"linux", "macosx"}
source = {
  url = "http://github.com/Kong/kong-plugin.git",
  tag = "0.1.0"
}

description = {
  summary = "Kong is a scalable and customizable API Management Layer built on top of Nginx.",
  homepage = "http://getkong.org",
  license = "Apache 2.0"
}

dependencies = {
}

build = {
  type = "builtin",
  modules = {
    ["kong.plugins."..package..".handler"] = "src/handler.lua",
    ["kong.plugins."..package..".schema"] = "src/schema.lua",
  }
}
