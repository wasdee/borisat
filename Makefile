pre:
	pipx install pdoc3

publish:
	poetry publish --build

generate_doc:
	pdoc --html borisat
