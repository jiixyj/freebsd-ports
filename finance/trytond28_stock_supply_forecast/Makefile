# Created by: Matthias Petermann <matthias@petermann-it.de>
# $FreeBSD$

PORTNAME=	trytond28_stock_supply_forecast
PORTVERSION=	2.8.0
CATEGORIES=	finance python
MASTER_SITES=	https://pypi.python.org/packages/source/t/trytond_stock_supply_forecast/ \
		http://downloads.tryton.org/${PORTVERSION:R}/
DISTNAME=	trytond_stock_supply_forecast-${PORTVERSION}

MAINTAINER=	matthias@petermann-it.de
COMMENT=	Tryton Application Platform (Stock Supply Forecast Module)

LICENSE=	GPLv3

RUN_DEPENDS=	trytond28_stock_supply>=2.8.1:${PORTSDIR}/finance/trytond28_stock_supply \
		trytond28_stock_forecast>=2.8.0:${PORTSDIR}/finance/trytond28_stock_forecast

CONFLICTS=	trytond_stock_supply_forecast-2.[46].*

USE_PYTHON=	yes
USE_PYDISTUTILS=easy_install
PYEASYINSTALL_EGG=${DISTNAME}-py${PYTHON_VER}${PYEASYINSTALL_OSARCH}.egg

.include <bsd.port.mk>
