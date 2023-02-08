def pytest_configure(config):
    config._metadata['Project Name'] = 'non Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester Name'] = 'Vinayak'

@pytest.mark.optionalhook
def pytesr_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Pluging", None)
