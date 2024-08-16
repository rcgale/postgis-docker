FROM postgis/postgis:15-3.4 as postgis

# get a copy of shp2pgsql
FROM postgis as builder

# This might require an occasional version bump. They use semantic versioning, so
# probably wise to stick to patch updates, and do minor/major updates only as needed
RUN apt-get update && apt-get install -y postgis=3.4.2+dfsg-1.pgdg110+1

# Postgis
FROM postgis

COPY --from=builder /usr/bin/shp2pgsql /usr/bin/

# Configure utils
RUN apt-get update \
    && apt-get install -y wget unzip \
    && rm -rf /var/lib/apt/lists/*

# Make data dir
RUN mkdir -p /gisdata \
    && chmod 777 -R /gisdata

# Copy nation an state scripts
COPY ./load_data.sh /docker-entrypoint-initdb.d/

# Overwrite the default /postgis.sh file
COPY ./postgis.sh /docker-entrypoint-initdb.d/
