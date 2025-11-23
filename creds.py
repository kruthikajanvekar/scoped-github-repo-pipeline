
githubClientID = "Ov23liMRm6s0nGUAd1EY"

# PostgreSQL settings (match these to your docker-compose.yml)
dbUser = "postgres"
dbPassword = "root"
dbHost = "db"                        # Should match your docker-compose service name (likely "db")
dbPort = "5432"
dbName = "kiaid"                  # Or whatever DB name you chose in docker-compose

# Redis settings (match to docker-compose service name)
redisHost = "cache"                  # Should match your docker-compose service name (likely "cache")
redisPort = "6379"
redisDB = "0"                        # Redis typically uses DB 0 (default)


