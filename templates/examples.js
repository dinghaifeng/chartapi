var is_debug = true;

function chartapi_do_render(e)
{
	engine = document.getElementById(e.id + "_engine").innerText;
	code = document.getElementById(e.id + "_code").innerText;
	if(is_debug) {
		var tag_element = document.createElement("div");
		tag_element.innerText = "Engine: " + engine;
		e.appendChild(tag_element);
		var tag_element = document.createElement("div");
		tag_element.innerText = "Code: ";
		e.appendChild(tag_element);
		var tag_element = document.createElement("pre");
		tag_element.innerText = code;
		e.appendChild(tag_element);
		var tag_element = document.createElement("div");
		tag_element.innerText = "Image: ";
		e.appendChild(tag_element);
	}
	img_element = document.createElement("img");
	img_element.src = "http://{{ HTTP_HOST }}/api/?engine=" + encodeURIComponent(engine) + "&code=" + encodeURIComponent(code);
	e.appendChild(img_element);
}

function chartapi_render_all()
{
	var graphs = document.getElementsByName("chartapi_canvas");
	for(i = 0; i < graphs.length; i++) {
		chartapi_do_render(graphs.item(i));
	}
}

chartapi_render_all();
