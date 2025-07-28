import { createDrawerNavigator } from '@react-navigation/drawer';
import React from 'react';
import Dashboard from '../components/Dashboard';
import Settings from '../components/Settings';

export type DrawerParamList = {
  Dashboard: undefined;
  Settings: undefined;
};

const Drawer = createDrawerNavigator<DrawerParamList>();

export default function DrawerNavigator() {
  return (
    <Drawer.Navigator initialRouteName="Dashboard">
      <Drawer.Screen name="Dashboard" component={Dashboard} />
      <Drawer.Screen name="Settings" component={Settings} />
    </Drawer.Navigator>
  );
}