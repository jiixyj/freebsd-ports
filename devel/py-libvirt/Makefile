# Created by: Jason Helfman <jgh@FreeBSD.org>
# $FreeBSD$

PORTNAME=	libvirt
PORTVERSION=	1.2.1
CATEGORIES=	devel
MASTER_SITES=	http://libvirt.org/sources/python/ \
		ftp://libvirt.org/libvirt/python/
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}
DISTNAME=	${PORTNAME}-python-${PORTVERSION}

MAINTAINER=	jgh@FreeBSD.org
COMMENT=	Python bindings for Libvirt virtualization API

LICENSE=	GPLv2

LIB_DEPENDS=	libvirt.so:${PORTSDIR}/devel/libvirt

USES=	pkgconfig shebangfix
SHEBANG_LANG=	python
SHEBANG_FILES=	generator.py sanitytest.py setup.py

USE_PYTHON_BUILD=	yes
USE_PYTHON_RUN=		yes
USE_PYDISTUTILS=	yes
PYDISTUTILS_NOEGGINFO=  yes
PYDISTUTILS_AUTOPLIST=	yes

post-patch-script:
	@${REINPLACE_CMD} -e 's|"python"|"${PYTHON_CMD}"|g' \
		${WRKSRC}/setup.py

post-install:
.for lib in libvirtmod libvirtmod_qemu libvirtmod_lxc
	@${STRIP_CMD} ${STAGEDIR}${PYTHON_LIBDIR}/site-packages/${lib}.so
.endfor

.include <bsd.port.mk>
