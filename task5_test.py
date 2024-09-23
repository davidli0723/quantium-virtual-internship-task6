from task4 import dash_app

def test_001_header(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#header", timeout=5)

def test_002_visualization(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#visualization", timeout=5)

def test_003_region_picker(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#region_picker", timeout=5)