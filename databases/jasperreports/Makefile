# Created by: Thierry Thomas <thierry@pompo.net>
# $FreeBSD$

PORTNAME=	jasperreports
PORTVERSION=	5.1.2
CATEGORIES=	databases print java
MASTER_SITES=	SF/${PORTNAME}/${PORTNAME}/JasperReports%20${PORTVERSION}
DISTFILES=	${PORTNAME}-${PORTVERSION}.jar ${PORTNAME}-applet-${PORTVERSION}.jar

MAINTAINER=	ports@FreeBSD.org
COMMENT=	JasperReports is a powerful open source Java reporting tool

RUN_DEPENDS=	${JAVALIBDIR}/itext.jar:${PORTSDIR}/devel/itext			\
		${JAVALIBDIR}/xalan.jar:${PORTSDIR}/textproc/xalan-j		\
		${JAVALIBDIR}/crimson.jar:${PORTSDIR}/textproc/crimson		\
		${JAVALIBDIR}/poi.jar:${PORTSDIR}/textproc/apache-poi		\
		${JAVALIBDIR}/jfreechart.jar:${PORTSDIR}/java/jfreechart	\
		${JAVASHAREDIR}/batik/batik.jar:${PORTSDIR}/graphics/batik	\
		${JAVALIBDIR}/commons-beanutils.jar:${PORTSDIR}/java/jakarta-commons-beanutils\
		${JAVALIBDIR}/commons-digester.jar:${PORTSDIR}/textproc/jakarta-commons-digester

OPTIONS_DEFINE=	MYSQL PGSQL ORACLE8 ORACLE9 HSQLDB
OPTIONS_DEFAULT=MYSQL PGSQL

ORACLE8_DESC=	Install libraries required for Oracle 8
ORACLE9_DESC=	Install libraries required for Oracle 9
HSQLDB_DESC=	Install libraries required for HSQLDB

USE_JAVA=	yes
JAVA_VERSION=	1.6+
NO_BUILD=	yes
EXTRACT_CMD=	${CP}
EXTRACT_BEFORE_ARGS=	# empty
EXTRACT_AFTER_ARGS=	.

LICENSE=	LGPL3

PLIST_FILES=	${DISTFILES:S|^|%%JAVAJARDIR%%/|:S|-${PORTVERSION}||}

.include <bsd.port.options.mk>

.if ${PORT_OPTIONS:MMYSQL}
RUN_DEPENDS+=	${JAVALIBDIR}/mysql-connector-java.jar:${PORTSDIR}/databases/mysql-connector-java
.else
RUN_DEPENDS+=	${JAVALIBDIR}/log4j.jar:${PORTSDIR}/devel/log4j
.endif

.if ${PORT_OPTIONS:MPGSQL}
RUN_DEPENDS+=	${JAVALIBDIR}/postgresql.jar:${PORTSDIR}/databases/postgresql-jdbc
.endif


.if ${PORT_OPTIONS:MORACLE8}
WITH_ORACLE8=	yes
RUN_DEPENDS+=	${JAVALIBDIR}/classes12.zip:${PORTSDIR}/databases/jdbc-oracle8i
.endif

.if ${PORT_OPTIONS:MORACLE9}
WITH_ORACLE9=	yes
RUN_DEPENDS+=	${JAVALIBDIR}/ojdbc14.jar:${PORTSDIR}/databases/jdbc-oracle9i
.endif

.if ${PORT_OPTIONS:MHSQLDB}
RUN_DEPENDS+=	${JAVALIBDIR}/hsqldb.jar:${PORTSDIR}/databases/hsqldb
.endif

post-extract:
.for jf in ${DISTFILES}
	${MV} ${WRKDIR}/${jf} ${WRKDIR}/${jf:S|-${PORTVERSION}||}
.endfor

do-install:
	${INSTALL_DATA} ${DISTFILES:S|^|${WRKDIR}/|:S|-${PORTVERSION}||}	\
		${STAGEDIR}${JAVAJARDIR}

.include <bsd.port.mk>
