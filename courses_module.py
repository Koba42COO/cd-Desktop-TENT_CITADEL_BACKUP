"""
Prestigious Higher Education Courses Module
Comprehensive database and management system for elite online courses
"""

from dataclasses import dataclass, asdict
from enum import Enum
from typing import List, Optional, Dict
import json


class CourseLevel(Enum):
    BEGINNER = "Beginner"
    INTERMEDIATE = "Intermediate"
    ADVANCED = "Advanced"
    PROFESSIONAL = "Professional"


class CourseFormat(Enum):
    INDIVIDUAL_COURSE = "Individual Course"
    CERTIFICATE_PROGRAM = "Certificate Program"
    MICRO_MASTERS = "Micro Masters"
    BACHELORS_DEGREE = "Bachelor's Degree"
    MASTERS_DEGREE = "Master's Degree"
    EXECUTIVE_EDUCATION = "Executive Education"


@dataclass
class Course:
    title: str
    provider: str
    university: str
    level: CourseLevel
    format: CourseFormat
    duration_weeks: int
    topics: List[str]
    description: str
    url: Optional[str] = None
    certification: bool = True
    price_usd: float = 0.0
    rating: float = 0.0
    learners: int = 0
    
    def to_dict(self) -> Dict:
        data = asdict(self)
        data['level'] = self.level.value
        data['format'] = self.format.value
        return data


class PrestigiousCoursesCatalog:
    def __init__(self):
        self.courses: List[Course] = []
        self._populate_elite_courses()
    
    def _populate_elite_courses(self):
        self.courses = [
            Course(
                title="CS50's Introduction to Computer Science",
                provider="edX", university="Harvard University",
                level=CourseLevel.BEGINNER, format=CourseFormat.INDIVIDUAL_COURSE,
                duration_weeks=12, topics=["C", "Python", "SQL", "JavaScript", "Web Development"],
                description="Introduction to computer science and programming.",
                url="https://www.edx.org/learn/computer-science/harvard-university-cs50",
                price_usd=199.0, rating=4.9, learners=3000000
            ),
            Course(
                title="AI: Implications for Business Strategy",
                provider="edX", university="MIT",
                level=CourseLevel.PROFESSIONAL, format=CourseFormat.EXECUTIVE_EDUCATION,
                duration_weeks=6, topics=["AI", "Machine Learning", "Business Strategy"],
                description="Executive education on AI's business impact.",
                price_usd=2950.0, rating=4.8, learners=15000
            ),
            Course(
                title="Probability: Science of Uncertainty and Data",
                provider="edX", university="MIT",
                level=CourseLevel.ADVANCED, format=CourseFormat.INDIVIDUAL_COURSE,
                duration_weeks=16, topics=["Probability", "Statistics", "Data Science"],
                description="Rigorous probability theory with data science applications.",
                price_usd=399.0, rating=4.9, learners=50000
            ),
            Course(
                title="Exercising Leadership: Foundational Principles",
                provider="edX", university="Harvard University",
                level=CourseLevel.PROFESSIONAL, format=CourseFormat.INDIVIDUAL_COURSE,
                duration_weeks=10, topics=["Leadership", "Management", "Ethics"],
                description="Foundations of leadership and personal development.",
                price_usd=299.0, rating=4.8, learners=40000
            ),
            Course(
                title="Machine Learning Specialization",
                provider="Coursera", university="Stanford University",
                level=CourseLevel.ADVANCED, format=CourseFormat.CERTIFICATE_PROGRAM,
                duration_weeks=12, topics=["Machine Learning", "Python", "Deep Learning"],
                description="Comprehensive ML specialization with practical projects.",
                price_usd=49.0, rating=4.9, learners=500000
            ),
            Course(
                title="Business Fundamentals",
                provider="Coursera", university="University of Pennsylvania (Wharton)",
                level=CourseLevel.BEGINNER, format=CourseFormat.CERTIFICATE_PROGRAM,
                duration_weeks=10, topics=["Business", "Finance", "Marketing", "Strategy"],
                description="Foundation for business professionals.",
                price_usd=49.0, rating=4.8, learners=400000
            ),
            Course(
                title="Deep Learning Specialization",
                provider="Coursera", university="Stanford University",
                level=CourseLevel.ADVANCED, format=CourseFormat.CERTIFICATE_PROGRAM,
                duration_weeks=16, topics=["Deep Learning", "Neural Networks", "TensorFlow"],
                description="Master deep learning fundamentals.",
                price_usd=49.0, rating=4.9, learners=800000
            ),
            Course(
                title="Master's in Data Science",
                provider="edX", university="UC San Diego",
                level=CourseLevel.PROFESSIONAL, format=CourseFormat.MASTERS_DEGREE,
                duration_weeks=96, topics=["Data Science", "Machine Learning", "Statistics"],
                description="Advanced degree in data science.",
                price_usd=20000.0, rating=4.8, learners=3000
            ),
        ]
    
    def get_courses_by_level(self, level: CourseLevel) -> List[Course]:
        return [c for c in self.courses if c.level == level]
    
    def get_courses_by_university(self, university: str) -> List[Course]:
        return [c for c in self.courses if university.lower() in c.university.lower()]
    
    def get_courses_by_topic(self, topic: str) -> List[Course]:
        return [c for c in self.courses if any(topic.lower() in t.lower() for t in c.topics)]
    
    def get_top_rated(self, limit: int = 5) -> List[Course]:
        return sorted(self.courses, key=lambda x: x.rating, reverse=True)[:limit]
    
    def get_most_popular(self, limit: int = 5) -> List[Course]:
        return sorted(self.courses, key=lambda x: x.learners, reverse=True)[:limit]
    
    def to_json(self) -> str:
        return json.dumps([c.to_dict() for c in self.courses], indent=2)
    
    def get_stats(self) -> Dict:
        return {
            "total_courses": len(self.courses),
            "avg_rating": sum(c.rating for c in self.courses) / len(self.courses),
            "total_learners": sum(c.learners for c in self.courses),
            "universities": list(set(c.university for c in self.courses))
        }


def main():
    catalog = PrestigiousCoursesCatalog()
    stats = catalog.get_stats()
    
    print("=" * 60)
    print("PRESTIGIOUS COURSES CATALOG")
    print("=" * 60)
    print(f"Total Courses: {stats['total_courses']}")
    print(f"Average Rating: {stats['avg_rating']:.2f}/5.0")
    print(f"Total Learners: {stats['total_learners']:,}")
    print(f"Universities: {', '.join(stats['universities'])}")
    
    print("\nTop Rated:")
    for c in catalog.get_top_rated(5):
        print(f"  • {c.title} ({c.university}) - {c.rating}/5.0")


if __name__ == "__main__":
    main()
