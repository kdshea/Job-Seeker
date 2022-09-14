import './styles/main.scss'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import NavBar from './components/NavBar'
import Footer from './components/Footer'
import Login from './components/Login'
import Register from './components/Register'
import Landing from './components/Landing'
import JobIndex from './components/JobIndex/JobIndex'
import AllActivities from './components/ActivityIndex/AllActivities'
import ActivitiesToday from './components/ActivityIndex/AllActivities'
import AddJobDetails from './components/AddJob/AddJobDetails'
import JobDetails from './components/Job/JobDetails'
import EditJobDetails from './components/EditJob/EditJobDetails'
import AddJobCompany from './components/AddJob/AddJobCompany'
import JobCompany from './components/Job/JobCompany'
import EditJobCompany from './components/EditJob/EditJobCompany'
import AddJobActivities from './components/AddJob/AddJobActivities'
import JobActivities from './components/Job/JobActivities'
import EditJobActivities from './components/EditJob/EditJobActivities'
import AddJobNote from './components/AddJob/AddJobNote'
import JobNote from './components/Job/JobNote'
import EditJobNote from './components/EditJob/EditJobNote'
import AddJobContacts from './components/AddJob/AddJobContact'
import JobContacts from './components/Job/JobContacts'
import EditJobContact from './components/EditJob/EditJobContact'

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <NavBar /> 
        <Routes>
          <Route path='/' element={<Landing />} />
          <Route path='/login' element={<Login />} />
          <Route path='/register' element={<Register />} />
          <Route path='/jobs' element={<JobIndex />} />
          <Route path='/activities' element={<AllActivities />} />
          <Route path='/activities/today' element={<ActivitiesToday />} />
          <Route path='/add-job' element={<AddJobDetails />} />
          <Route path='/jobs/:jobId' element={<JobDetails />} />
          <Route path='/edit-job/:jobId' element={<EditJobDetails />} />
          <Route path='/add-job/:jobId/company' element={<AddJobCompany />} />
          <Route path='/jobs/:jobId/company' element={<JobCompany />} />
          <Route path='/edit-company/job:jobId/:companyId' element={<EditJobCompany />} />
          <Route path='/add-job/:jobId/activities' element={<AddJobActivities />} />
          <Route path='/jobs/:jobId/activities' element={<JobActivities />} />
          <Route path='/edit-activity/job:jobId/:activityId' element={<EditJobActivities />} />
          <Route path='/add-job/:jobId/note' element={<AddJobNote />} />
          <Route path='/jobs/:jobId/notes' element={<JobNote />} />
          <Route path='/edit-note/job:jobId/:noteId' element={<EditJobNote />} />
          <Route path='/add-job/:jobId/contacts' element={<AddJobContacts />} />
          <Route path='/jobs/:jobId/contacts' element={<JobContacts />} />
          <Route path='/edit-contact/job:jobId/:contactId' element={<EditJobContact />} />

          
        </Routes>
        <Footer />
      </BrowserRouter>
    </div>
  )
}

export default App
