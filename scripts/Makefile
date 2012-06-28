
indices: ../index/index.conf ../index/index.xml ../index/index.json

../index/index.conf: index.conf.in
	python genindex $< ../colorschemes/*.conf > $@

../index/index.xml: index.xml.in
	python genindex $< ../colorschemes/*.conf > $@

../index/index.json: index.json.in
	python genindex $< ../colorschemes/*.conf > $@

clean:
	rm -f ../index/index.conf ../index/index.xml ../index/index.json

.PHONY: indices clean
