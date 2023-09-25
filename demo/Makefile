PluginName = demo
PluginVersion = 1.0.0-0
ContainerName = kong-${PluginName}
KongImage = docker.io/library/kong:2.3.3

all: clean build-pack

clean:
	rm -rf rockpack/*.rock

build:
	luarocks make rockspec/${PluginName}-${PluginVersion}.rockspec
	luarocks pack ${PluginName} ${PluginVersion}
	mv ${PluginName}-${PluginVersion}.all.rock rockpack

kong-start:
	@docker run --rm --detach --name ${ContainerName} \
	--network=host \
	-w /home/kong \
	-e "KONG_ADMIN_LISTEN=0.0.0.0:8001" \
	-e "KONG_PROXY_LISTEN=0.0.0.0:8000" \
	-e "KONG_DATABASE=off" \
	-e "KONG_LOG_LEVEL"="debug" \
	${KongImage}

kong-stop:
	@docker stop ${ContainerName}

kong-plugin:
	docker cp rockpack ${ContainerName}:/home/kong
	ls rockpack |grep rock$$ | xargs -t -I {} docker exec -i --user root ${ContainerName} luarocks install rockpack/{}
	docker exec --user kong -e KONG_PLUGINS="bundled,${PluginName}" ${ContainerName} kong reload -vv

check-plugin:
	python check-plugin.py ${PluginName}

kong-server:
	curl -X POST http://localhost:8001/config -F config=@test/server.yml

check-server:
	python test/check-server.py

kong-attach:
	docker exec -it -u kong ${ContainerName} bash

kong-monitor:
	docker logs -f --tail 10 ${ContainerName}
