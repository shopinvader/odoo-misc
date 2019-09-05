import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-shopinvader-odoo-misc",
    description="Meta package for shopinvader-odoo-misc Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-base_sparse_field_list_support',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
