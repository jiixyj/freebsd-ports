# Created by: Sergey Skvortsov <skv@protey.ru>
# $FreeBSD$

PORTNAME=	skytools
PORTVERSION=	2.1.12
PORTREVISION=	1
CATEGORIES=	databases
MASTER_SITES=	http://pgfoundry.org/frs/download.php/2872/

MAINTAINER=	kheechin@gmail.com
COMMENT=	PostgreSQL tools from Skype: walshipping, queueing, replication

GNU_CONFIGURE=	yes
USES=		gmake shebangfix

USE_PGSQL=	yes
WANT_PGSQL_VER=	91-
USE_PYTHON=	2
INSTALLS_EGGINFO=	yes

python_OLD_CMD=	/usr/bin/env python
python_CMD=	/usr/bin/env python2
SHEBANG_FILES=	scripts/catsql.py scripts/bulk_loader.py \
		scripts/cube_dispatcher.py scripts/queue_splitter.py \
		scripts/queue_mover.py scripts/scriptmgr.py \
		scripts/skytools_upgrade.py scripts/table_dispatcher.py

MAN1=	bulk_loader.1 cube_dispatcher.1 londiste.1 pgqadm.1 queue_mover.1 \
	queue_splitter.1 scriptmgr.1 skytools_upgrade.1 table_dispatcher.1 \
	walmgr.1
MAN5=	londiste.5

CONFIGURE_ARGS=	--with-python=${PYTHON_CMD} \
		--docdir=${EXAMPLESDIR} \
		--with-pgconfig=${LOCALBASE}/bin/pg_config

NO_STAGE=	yes
post-patch:
	@${REINPLACE_CMD} -e 's=share/doc=share/examples=' ${WRKSRC}/setup.py

.include <bsd.port.mk>
