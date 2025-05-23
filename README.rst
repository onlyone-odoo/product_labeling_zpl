===========
Product Labeling
===========

.. |badge1| image:: https://img.shields.io/badge/maturity-Stable-brightgreen
    :target: https://odoo-community.org/page/development-status
    :alt: Stable
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3

.. |badge3| image:: https://onlyone.odoo.com/web/image/website/1/logo/OnlyOne%20Soft?unique=dccda5b
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3

|badge1| |badge2| |badge3|

This module extends the functionality of the Manufacturing (MRP) module in Odoo 17 to support the generation of custom ZPL labels (ETI-CORTA, ETI-MEDIA, ETI-LARGA, ETI-CAJA) directly from manufacturing orders. It allows you to print product labels with batch information, such as lot number, manufacturing date, and expiration date, using Zebra printers.

**Table of contents**

.. contents::
   :local:

Install
=======

To install this module, you need to:

1. Clone or download the module into your Odoo addons directory.
2. Update the Odoo module list from the Odoo interface (Apps > Update Apps List).
3. Search for "Product Labeling" in the Apps menu and click "Install".
4. Ensure that the dependencies (`product`, `stock`, and `mrp`) are already installed.

.. note:: This module generates ZPL files for Zebra printers. To send the ZPL directly to a printer, you may need to configure a print server (e.g., CUPS) or use a connector compatible with your Zebra printer.

Configure
=========

To configure this module, you need to:

1. Go to **Manufacturing > Configuration > Settings** and ensure that lot tracking is enabled for your products.
2. Configure your products in **Inventory > Products > Products** to include the necessary information (e.g., name, tracking by lots).
3. Set up your Zebra printer in your system (e.g., via CUPS) if you plan to send ZPL directly to the printer instead of downloading the file.

Usage
=====

1. Go to **Manufacturing > Operations > Manufacturing Orders**.
2. Create or select a manufacturing order and confirm it to start production.
3. Once the production is confirmed and a lot is assigned (via `lot_producing_id`), click on "Print Labels" from the manufacturing order form.
4. In the wizard that appears, select the label type (ETI-CORTA, ETI-MEDIA, ETI-LARGA, or ETI-CAJA).
5. The wizard will automatically populate the lot number, manufacturing date, expiration date, and quantity based on the manufacturing order.
6. Click "Print" to generate a ZPL file containing the labels (one label per unit produced).
7. Download the ZPL file and send it to your Zebra printer, or use a configured print server to print directly.

Known issues / Roadmap
======================

* **Known Issues**: 
  - Direct printing to Zebra printers requires additional configuration (e.g., CUPS or a custom connector), which is not included in this module.
  - The expiration date is currently calculated as 2 years from the manufacturing date; this logic may need customization based on specific product requirements.

* **Roadmap**:
  - Add support for direct printing to Zebra printers via a configurable connector.
  - Allow customization of label designs through a user interface in Odoo.
  - Support for additional label types or dynamic sizing based on product attributes.

Bug Tracker
===========

Bugs are tracked on our website. In case of trouble, please check there if your issue has already been reported. If you need further assistance, please contact us.

* **Help Contact**: `Be OnlyOne Support <https://onlyone.odoo.com/contact>`_

Credits
=======

Authors
~~~~~~~

* Be OnlyOne

Contributors
~~~~~~~~~~~~

* `Be OnlyOne <https://onlyone.odoo.com/>`_
  
  * Matías Bressanello

Maintainers
~~~~~~~~~~~

This module is maintained by Be OnlyOne.