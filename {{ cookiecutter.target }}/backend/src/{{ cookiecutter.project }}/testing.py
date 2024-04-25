from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneWithPackageLayer

import {{ cookiecutter.project }}

BASENAME = "{{ cookiecutter.project | capitalize }}Layer"

# some dependencies may need to be initialised as a product
PRODUCTS = ["{{ cookiecutter.project }}"]

FIXTURE = PloneWithPackageLayer(
    bases=(PLONE_APP_CONTENTTYPES_FIXTURE,),
    name=f"{BASENAME}:Fixture",
    gs_profile_id="voltoweb:default",
    zcml_package=voltoweb,
    zcml_filename="configure.zcml",
    additional_z2_products=PRODUCTS,
)


INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,), name=f"{BASENAME}:IntegrationTesting",
)


FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,), name=f"{BASENAME}:FunctionalTesting",
)
