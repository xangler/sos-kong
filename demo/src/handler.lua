local DemoHandler = {
  PRIORITY = 100,
  VERSION = "1.0.0"
}

function DemoHandler:access(conf)
  if kong.request.get_header("X-Hello") == conf.user then
    kong.log.debug("found header hello" )
  else
    kong.response.exit(404, '{"error": "No found header hello"}')
  end
end

return DemoHandler
