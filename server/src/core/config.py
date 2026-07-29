"""Application settings — the single source of truth for all configuration.

Every field maps 1:1 to a variable in server/.env.example. Secrets default to
empty strings so the app boots without them; pipeline entry points call
missing_integration_keys() and fail fast with a clear message instead.
"""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # --- App ---
    app_env: str = "development"
    api_base_url: str = "http://localhost:8000"
    frontend_origin: str = "http://localhost:3000"
    database_url: str = "sqlite+aiosqlite:///./msk_leads.db"
    log_level: str = "INFO"

    # --- LLM (research, scoring, email drafts) ---
    llm_provider: str = "openai"
    llm_api_key: str = ""
    llm_model: str = "gpt-4.1-mini"
    llm_email_model: str = "gpt-4.1"
    llm_max_retries: int = 3
    llm_request_timeout_seconds: int = 60

    # --- Google Places (New) ---
    google_places_api_key: str = ""
    places_page_size: int = 20
    places_max_pages_per_query: int = 2
    places_request_delay_ms: int = 200

    # --- Firecrawl ---
    firecrawl_api_key: str = ""
    firecrawl_timeout_ms: int = 120000
    firecrawl_max_age_ms: int = 604800000

    # --- Google Sheets export (optional in v1) ---
    google_service_account_json_path: str = "./secrets/service-account.json"
    google_sheets_spreadsheet_id: str = ""

    # --- Pipeline guardrails ---
    max_discovery_queries_per_run: int = 32
    max_research_concurrency: int = 3
    score_auto_accept_threshold: int = 70
    score_reject_threshold: int = 40

    def missing_integration_keys(self) -> list[str]:
        """Return env var names that must be set before a pipeline run starts."""
        required_keys = {
            "LLM_API_KEY": self.llm_api_key,
            "GOOGLE_PLACES_API_KEY": self.google_places_api_key,
            "FIRECRAWL_API_KEY": self.firecrawl_api_key,
        }
        return [name for name, value in required_keys.items() if not value]


@lru_cache
def get_app_settings() -> AppSettings:
    return AppSettings()
