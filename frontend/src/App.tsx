import { GraduationCap, BookOpen, Users, Award } from 'lucide-react';

function App() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-50 via-white to-purple-50">
      {/* Navigation */}
      <nav className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16 items-center">
            <div className="flex items-center">
              <GraduationCap className="h-8 w-8 text-indigo-600" />
              <span className="ml-2 text-xl font-bold text-gray-900">EduTech</span>
            </div>
            <div className="hidden sm:flex sm:space-x-8">
              <a href="#" className="text-gray-900 hover:text-indigo-600 px-3 py-2 font-medium">Home</a>
              <a href="#" className="text-gray-500 hover:text-indigo-600 px-3 py-2 font-medium">Courses</a>
              <a href="#" className="text-gray-500 hover:text-indigo-600 px-3 py-2 font-medium">Resources</a>
              <a href="#" className="text-gray-500 hover:text-indigo-600 px-3 py-2 font-medium">Contact</a>
            </div>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <div className="relative overflow-hidden">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24">
          <div className="text-center">
            <h1 className="text-4xl tracking-tight font-extrabold text-gray-900 sm:text-5xl md:text-6xl">
              <span className="block">Transform Education</span>
              <span className="block text-indigo-600">With AI-Powered Learning</span>
            </h1>
            <p className="mt-3 max-w-md mx-auto text-base text-gray-500 sm:text-lg md:mt-5 md:text-xl md:max-w-3xl">
              Empower students with personalized learning experiences through cutting-edge artificial intelligence and expert educational content.
            </p>
            <div className="mt-5 max-w-md mx-auto sm:flex sm:justify-center md:mt-8">
              <div className="rounded-md shadow">
                <a href="#" className="w-full flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 md:py-4 md:text-lg md:px-10">
                  Get Started
                </a>
              </div>
              <div className="mt-3 rounded-md shadow sm:mt-0 sm:ml-3">
                <a href="#" className="w-full flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-indigo-600 bg-white hover:bg-gray-50 md:py-4 md:text-lg md:px-10">
                  Learn More
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Features Section */}
      <div className="py-12 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-3">
            <div className="relative p-6 bg-white rounded-lg shadow-sm hover:shadow-md transition-shadow">
              <div className="absolute top-6 right-6">
                <BookOpen className="h-6 w-6 text-indigo-600" />
              </div>
              <h3 className="text-lg font-medium text-gray-900">Personalized Learning</h3>
              <p className="mt-2 text-base text-gray-500">
                AI-driven content adaptation to match each student's learning style and pace.
              </p>
            </div>
            <div className="relative p-6 bg-white rounded-lg shadow-sm hover:shadow-md transition-shadow">
              <div className="absolute top-6 right-6">
                <Users className="h-6 w-6 text-indigo-600" />
              </div>
              <h3 className="text-lg font-medium text-gray-900">Collaborative Tools</h3>
              <p className="mt-2 text-base text-gray-500">
                Interactive features that enable seamless collaboration between students and teachers.
              </p>
            </div>
            <div className="relative p-6 bg-white rounded-lg shadow-sm hover:shadow-md transition-shadow">
              <div className="absolute top-6 right-6">
                <Award className="h-6 w-6 text-indigo-600" />
              </div>
              <h3 className="text-lg font-medium text-gray-900">Progress Tracking</h3>
              <p className="mt-2 text-base text-gray-500">
                Comprehensive analytics and insights to monitor student achievement.
              </p>
            </div>
          </div>
        </div>
      </div>

      {/* Footer */}
      <footer className="bg-gray-50">
        <div className="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center">
            <div className="flex items-center">
              <GraduationCap className="h-8 w-8 text-indigo-600" />
              <span className="ml-2 text-xl font-bold text-gray-900">EduTech</span>
            </div>
            <p className="text-gray-500 text-sm">© 2024 EduTech. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;