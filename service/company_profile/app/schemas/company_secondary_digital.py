from pydantic import BaseModel

class CompanySecondaryBase(BaseModel):
    twitter_handle: str | None
    facebook_page_url: str | None
    instagram_page_url: str | None
    key_business_leaders_name: str | None
    key_business_leaders_linkedin_url: str | None
    regulatory_licenses_certifications: str | None
    compliance_track_record: str | None
    legal_issues_controversies: str | None
    processing_time: str | None
    success_rate: str | None

class CompanySecondaryCreateUpdate(CompanySecondaryBase):
    pass

class CompanySecondaryRead(CompanySecondaryBase):
    company_id: int

    class Config:
        from_attributes = True

class DigitalPresenceBrandBase(BaseModel):
    quality_of_website: str | None
    awards_recognition: str | None
    brand_sentiment_score: str | None
    news_about_company: str | None
    average_deal_size: str | None
    top_customers: str | None
    website_traffic_rank: str | None
    social_media_followers_combined: str | None
    glassdoor_rating: str | None
    indeed_rating: str | None
    google_reviews_rating: str | None

class DigitalPresenceBrandCreateUpdate(DigitalPresenceBrandBase):
    pass

class DigitalPresenceBrandRead(DigitalPresenceBrandBase):
    company_id: int

    class Config:
        from_attributes = True
