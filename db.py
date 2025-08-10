from supabase import create_client

# Substitua pelos seus valores do passo 3
SUPABASE_URL = "https://ryvvjenayolflezqjogs.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJ5dnZqZW5heW9sZmxlenFqb2dzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTQ3NzI2MzEsImV4cCI6MjA3MDM0ODYzMX0.6-cuQcTdNIBnxR2VO38y7I15TYXfKN_OiasZxeAy_U4"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

print("Conectado!")