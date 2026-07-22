from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.sql import func
from database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(String, primary_key=True, index=True)
    title = Column(String, nullable=False)
    category = Column(String, nullable=False)
    problem = Column(String, nullable=False)
    contribution = Column(String, nullable=False)
    result = Column(String, nullable=False)
    techStack = Column(ARRAY(String))
    liveUrl = Column(String, nullable=True)
    caseStudyUrl = Column(String, nullable=True)
    imageUrl = Column(String, nullable=True)
    featured = Column(Boolean, default=False)
    order = Column(Integer, default=0)
    visible = Column(Boolean, default=True)
    createdAt = Column(DateTime, default=func.now())

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, default=1)
    name = Column(String, default="Khashia Zahira Suharlan")
    role = Column(String, default="AI Engineer • Machine Learning • Data Science")
    tagline = Column(String, default="Building healthcare-focused intelligent systems.")
    aboutTitle = Column(String, default="What drives me")
    aboutBody = Column(String)
    location = Column(String, default="Cikarang, Indonesia")
    email = Column(String, nullable=True)
    linkedin = Column(String, nullable=True)
    github = Column(String, nullable=True)
    instagram = Column(String, nullable=True)
    cvUrl = Column(String, nullable=True)
    photoUrl = Column(String, nullable=True)
    updatedAt = Column(DateTime, default=func.now(), onupdate=func.now())

class Experience(Base):
    __tablename__ = "experiences"

    id = Column(String, primary_key=True, index=True)
    title = Column(String, nullable=False)
    company = Column(String, nullable=False)
    employmentType = Column(String, nullable=False)
    location = Column(String, nullable=True)
    startDate = Column(String, nullable=False)
    endDate = Column(String, nullable=True)
    responsibilities = Column(String, nullable=True)
    achievements = Column(String, nullable=True)
    techStack = Column(ARRAY(String))
    imageUrl = Column(String, nullable=True)
    order = Column(Integer, default=0)
    visible = Column(Boolean, default=True)
    createdAt = Column(DateTime, default=func.now())

class Education(Base):
    __tablename__ = "educations"

    id = Column(String, primary_key=True, index=True)
    institution = Column(String, nullable=False)
    degree = Column(String, nullable=False)
    major = Column(String, nullable=True)
    location = Column(String, nullable=True)
    startDate = Column(String, nullable=False)
    endDate = Column(String, nullable=True)
    currentStudent = Column(Boolean, default=False)
    gpa = Column(String, nullable=True)
    overview = Column(String, nullable=True)
    courses = Column(ARRAY(String))
    achievements = Column(String, nullable=True)
    activities = Column(String, nullable=True)
    skills = Column(ARRAY(String))
    imageUrl = Column(String, nullable=True)
    order = Column(Integer, default=0)

class Certification(Base):
    __tablename__ = "certifications"

    id = Column(String, primary_key=True, index=True)
    title = Column(String, nullable=False)
    issuer = Column(String, nullable=False)
    date = Column(String, nullable=False)
    url = Column(String, nullable=True)
    imageUrl = Column(String, nullable=True)   # <-- BARU
    order = Column(Integer, default=0)
    visible = Column(Boolean, default=True)