scheme_files = $(wildcard ../colorschemes/*.conf)
screen_files = $(wildcard ../screenshots/*.png)

all: index.json index.json.md5

index.json: $(scheme_files) $(screen_files)
	python ../scripts/mkindex.py > $@

index.json.md5: index.json
	md5sum $< > $@

clean:
	rm -f index.json*

.PHONY: all clean
