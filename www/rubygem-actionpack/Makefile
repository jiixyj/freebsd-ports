# Created by: Jonathan Weiss (<jw@innerewut.de>)
# $FreeBSD$

PORTNAME=	actionpack
PORTVERSION=	3.2.16
PORTREVISION=	1
CATEGORIES=	www rubygems
MASTER_SITES=	RG

MAINTAINER=	ruby@FreeBSD.org
COMMENT=	Action Controller and Action View of Rails MVC Framework

LICENSE=	MIT

RUN_DEPENDS=	rubygem-activemodel>=${PORTVERSION}:${PORTSDIR}/databases/rubygem-activemodel \
		rubygem-activesupport>=${PORTVERSION}:${PORTSDIR}/devel/rubygem-activesupport \
		rubygem-builder>=3.0.0:${PORTSDIR}/devel/rubygem-builder \
		rubygem-erubis>=2.7.0:${PORTSDIR}/www/rubygem-erubis \
		rubygem-journey>=1.0.4:${PORTSDIR}/www/rubygem-journey \
		rubygem-rack>=1.4.5:${PORTSDIR}/www/rubygem-rack \
		rubygem-rack-cache>=1.2:${PORTSDIR}/www/rubygem-rack-cache \
		rubygem-rack-test>=0.6.1:${PORTSDIR}/www/rubygem-rack-test \
		rubygem-sprockets>=2.2.1:${PORTSDIR}/devel/rubygem-sprockets

USE_RUBY=	yes
USE_RUBYGEMS=	yes
RUBYGEM_AUTOPLIST=	yes

post-patch:
	@${REINPLACE_CMD} -e '115 s|~>|>=|' ${WRKSRC}/${GEM_NAME}.gemspec

.include <bsd.port.mk>
