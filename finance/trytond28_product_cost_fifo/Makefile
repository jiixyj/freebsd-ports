# Created by: Matthias Petermann <matthias@petermann-it.de>
# $FreeBSD$

PORTNAME=	trytond28_product_cost_fifo
PORTVERSION=	2.8.1
CATEGORIES=	finance python
MASTER_SITES=	https://pypi.python.org/packages/source/t/trytond_product_cost_fifo/ \
		http://downloads.tryton.org/${PORTVERSION:R}/
DISTNAME=	trytond_product_cost_fifo-${PORTVERSION}

MAINTAINER=	matthias@petermann-it.de
COMMENT=	Tryton Application Platform (Product Cost Fifo Module)

LICENSE=	GPLv3

RUN_DEPENDS=	trytond28_product>=2.8.0:${PORTSDIR}/finance/trytond28_product \
		trytond28_stock>=2.8.2:${PORTSDIR}/finance/trytond28_stock

CONFLICTS=	trytond_product_cost_fifo-2.[46].*

USE_PYTHON=	yes
USE_PYDISTUTILS=easy_install
PYEASYINSTALL_EGG=${DISTNAME}-py${PYTHON_VER}${PYEASYINSTALL_OSARCH}.egg

.include <bsd.port.mk>
