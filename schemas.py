from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# --- Project Schemas ---
class ProjectBase(BaseModel):
    title: str
    category: str
    problem: str
    contribution: str
    result: str
    techStack: List[str]
    liveUrl: Optional[str] = None
    caseStudyUrl: Optional[str] = None
    imageUrl: Optional[str] = None
    featured: bool = False
    order: int = 0
    visible: bool = True

class ProjectCreate(ProjectBase):
    pass

class ProjectResponse(ProjectBase):
    id: str
    createdAt: datetime
    class Config:
        from_attributes = True

class ProjectUpdate(BaseModel):
    title: Optional[str] = None
    category: Optional[str] = None
    problem: Optional[str] = None
    contribution: Optional[str] = None
    result: Optional[str] = None
    techStack: Optional[List[str]] = None
    liveUrl: Optional[str] = None
    caseStudyUrl: Optional[str] = None
    imageUrl: Optional[str] = None
    featured: Optional[bool] = None
    order: Optional[int] = None
    visible: Optional[bool] = None

# --- Profile Schemas ---
class ProfileUpdate(BaseModel):
    name: Optional[str] = None
    role: Optional[str] = None
    tagline: Optional[str] = None
    aboutTitle: Optional[str] = None
    aboutBody: Optional[str] = None
    location: Optional[str] = None
    email: Optional[str] = None
    linkedin: Optional[str] = None
    github: Optional[str] = None
    instagram: Optional[str] = None
    cvUrl: Optional[str] = None
    photoUrl: Optional[str] = None

    class Config:
        from_attributes = True

# --- Experience Schemas ---
class ExperienceBase(BaseModel):
    title: str
    company: str
    employmentType: str
    location: Optional[str] = None
    startDate: str
    endDate: Optional[str] = None
    responsibilities: Optional[str] = None
    achievements: Optional[str] = None
    techStack: List[str] = []
    imageUrl: Optional[str] = None
    order: int = 0
    visible: bool = True

class ExperienceCreate(ExperienceBase):
    pass

class ExperienceResponse(ExperienceBase):
    id: str
    createdAt: datetime
    class Config:
        from_attributes = True

class ExperienceUpdate(BaseModel):
    title: Optional[str] = None
    company: Optional[str] = None
    employmentType: Optional[str] = None
    location: Optional[str] = None
    startDate: Optional[str] = None
    endDate: Optional[str] = None
    responsibilities: Optional[str] = None
    achievements: Optional[str] = None
    techStack: Optional[List[str]] = None
    imageUrl: Optional[str] = None
    order: Optional[int] = None
    visible: Optional[bool] = None

# --- Education Schemas ---
class EducationBase(BaseModel):
    institution: str
    degree: str
    major: Optional[str] = None
    location: Optional[str] = None
    startDate: str
    endDate: Optional[str] = None
    currentStudent: bool = False
    gpa: Optional[str] = None
    overview: Optional[str] = None
    courses: List[str] = []
    achievements: Optional[str] = None
    activities: Optional[str] = None
    skills: List[str] = []
    imageUrl: Optional[str] = None
    order: int = 0

class EducationCreate(EducationBase):
    pass

class EducationResponse(EducationBase):
    id: str
    class Config:
        from_attributes = True

class EducationUpdate(BaseModel):
    institution: Optional[str] = None
    degree: Optional[str] = None
    major: Optional[str] = None
    location: Optional[str] = None
    startDate: Optional[str] = None
    endDate: Optional[str] = None
    currentStudent: Optional[bool] = None
    gpa: Optional[str] = None
    overview: Optional[str] = None
    courses: Optional[List[str]] = None
    achievements: Optional[str] = None
    activities: Optional[str] = None
    skills: Optional[List[str]] = None
    imageUrl: Optional[str] = None
    order: Optional[int] = None

# --- Certification Schemas ---
class CertificationBase(BaseModel):
    title: str
    issuer: str
    date: str
    url: Optional[str] = None
    imageUrl: Optional[str] = None
    order: int = 0
    visible: bool = True

class CertificationCreate(CertificationBase):
    pass

class CertificationResponse(CertificationBase):
    id: str
    class Config:
        from_attributes = True

class CertificationUpdate(BaseModel):
    title: Optional[str] = None
    issuer: Optional[str] = None
    date: Optional[str] = None
    url: Optional[str] = None
    imageUrl: Optional[str] = None
    order: Optional[int] = None
    visible: Optional[bool] = None